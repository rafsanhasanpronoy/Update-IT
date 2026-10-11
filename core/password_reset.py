from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm


class StaffPasswordResetForm(PasswordResetForm):
    """Send recovery links only to active staff accounts with usable passwords."""

    def get_users(self, email):
        User = get_user_model()
        email_field = User.get_email_field_name()
        users = User._default_manager.filter(
            **{
                f"{email_field}__iexact": email,
                "is_active": True,
                "is_staff": True,
            }
        )
        return (user for user in users if user.has_usable_password())
