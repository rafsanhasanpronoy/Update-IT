import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = (
        "Create the initial Django superuser if it does not exist. "
        "Does not overwrite an existing account or its password."
    )

    def handle(self, *args, **options):
        password = os.environ.get("DJANGO_BOOTSTRAP_ADMIN_PASSWORD", "")
        email = os.environ.get("DJANGO_BOOTSTRAP_ADMIN_EMAIL", "").strip()
        username = os.environ.get("DJANGO_BOOTSTRAP_ADMIN_USERNAME", "pronoy").strip()

        # Keep ordinary deploys safe: without the explicit password, do nothing.
        if not password:
            self.stdout.write("Initial admin bootstrap skipped (password variable not set).")
            return

        if not username:
            raise CommandError("DJANGO_BOOTSTRAP_ADMIN_USERNAME must not be empty.")
        if not email:
            raise CommandError(
                "Set DJANGO_BOOTSTRAP_ADMIN_EMAIL to a real mailbox so password recovery can work."
            )

        User = get_user_model()
        existing = User._default_manager.filter(**{User.USERNAME_FIELD: username}).first()
        if existing:
            self.stdout.write(
                self.style.WARNING(
                    f"Account '{username}' already exists; its password and permissions were not changed."
                )
            )
            return

        user = User._default_manager.create_user(
            **{User.USERNAME_FIELD: username},
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.stdout.write(self.style.SUCCESS(f"Initial admin '{username}' created."))
