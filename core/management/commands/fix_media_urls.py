"""
Repair stored Supabase media URLs after changing the project's bucket/project.

Safe by default: this command only reports candidates unless --apply is passed.
It updates URL fields in the production database configured by Django.

Run:
    python manage.py fix_media_urls          # dry run
    python manage.py fix_media_urls --apply  # save repaired URLs

Only Supabase Storage URLs whose bucket is update-it or update-it-media are
considered. External image URLs and local /media/ paths are left untouched.
The objects themselves are not moved or uploaded; they must already exist in
the target 'update-it' bucket at the same relative key.
"""
from urllib.parse import urlsplit

from django.core.management.base import BaseCommand

from core.models import Achievement, Faculty, Gallery, Student

TARGET_PROJECT = "rscxskiekqhbjjsnatmf"
TARGET_BUCKET = "update-it"
TARGET_PUBLIC_PREFIX = (
    f"https://{TARGET_PROJECT}.supabase.co/storage/v1/object/public/{TARGET_BUCKET}/"
)
KNOWN_BUCKETS = {"update-it", "update-it-media"}
FIELDS = [
    (Achievement, "image_url"),
    (Faculty, "photo_url"),
    (Gallery, "image_url"),
    (Student, "photo_url"),
]


def repaired_url(value):
    """Return the target public URL for a known Supabase Storage URL, else None."""
    if not value or not isinstance(value, str):
        return None

    parsed = urlsplit(value.strip())
    host = (parsed.hostname or "").lower()
    if "supabase.co" not in host:
        return None

    path = parsed.path.lstrip("/")
    markers = (
        "storage/v1/object/public/",
        "storage/v1/object/sign/",
        "storage/v1/object/",
        "storage/v1/s3/",
    )
    for marker in markers:
        if path.startswith(marker):
            remainder = path[len(marker):]
            bucket, separator, key = remainder.partition("/")
            if separator and bucket in KNOWN_BUCKETS and key:
                # Keep the object key as-is, including subfolders such as students/.
                return TARGET_PUBLIC_PREFIX + key

    return None


class Command(BaseCommand):
    help = "Report or repair Supabase Storage URLs saved in image URL fields."

    def add_arguments(self, parser):
        parser.add_argument(
            "--apply",
            action="store_true",
            help="Save URL changes. Without this flag, the command is a dry run.",
        )

    def handle(self, *args, **options):
        apply_changes = options["apply"]
        candidates = 0
        changed = 0

        for model, field in FIELDS:
            self.stdout.write(f"\\n--- {model.__name__}.{field} ---")
            for obj in model.objects.exclude(**{f"{field}__isnull": True}).exclude(**{field: ""}).iterator():
                old_value = getattr(obj, field)
                new_value = repaired_url(old_value)
                if not new_value or new_value == old_value:
                    continue

                candidates += 1
                self.stdout.write(
                    f"  [{'APPLY' if apply_changes else 'DRY RUN'}] "
                    f"id={obj.pk}: {old_value} -> {new_value}"
                )
                if apply_changes:
                    setattr(obj, field, new_value)
                    obj.save(update_fields=[field])
                    changed += 1

        self.stdout.write("\\n--- Summary ---")
        self.stdout.write(f"Candidate URLs: {candidates}")
        self.stdout.write(f"Updated URLs: {changed}")
        if not apply_changes:
            self.stdout.write(
                self.style.WARNING(
                    "Dry run only. Review the listed URLs, then rerun with --apply to save them."
                )
            )
        self.stdout.write(
            self.style.WARNING(
                "This command changes database URL strings only. It does not copy objects between buckets."
            )
        )
