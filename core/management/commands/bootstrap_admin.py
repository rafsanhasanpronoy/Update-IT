import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = (
        "Create or repair the initial Django superuser when an explicit "
        "bootstrap password is configured."
    )

    def handle(self, *args, **options):
        password = os.environ.get("DJANGO_BOOTSTRAP_ADMIN_PASSWORD", "")
        email = os.environ.get("DJANGO_BOOTSTRAP_ADMIN_EMAIL", "").strip()
        username = os.environ.get("DJANGO_BOOTSTRAP_ADMIN_USERNAME", "pronoy").strip()

        # Without an explicit password, leave all accounts untouched.
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
        user = User._default_manager.filter(
            **{User.USERNAME_FIELD: username}
        ).first()

        if user is None:
            user = User._default_manager.create_user(
                **{User.USERNAME_FIELD: username},
                email=email,
                password=password,
            )
            action = "created"
        else:
            # This reset is intentional only when the bootstrap password is set.
            user.set_password(password)
            user.email = email
            action = "updated"

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()

        self.stdout.write(
            self.style.SUCCESS(f"Initial admin '{username}' {action} successfully.")
        )
