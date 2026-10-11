#!/bin/bash
set -e

python manage.py collectstatic --noinput
python manage.py migrate

# Creates the initial admin only when DJANGO_BOOTSTRAP_ADMIN_PASSWORD and
# DJANGO_BOOTSTRAP_ADMIN_EMAIL are set. The command never resets an existing
# account's password. Configure these as Render environment variables and
# remove the password variable after the first successful deployment.
python manage.py bootstrap_admin

gunicorn config.wsgi --bind 0.0.0.0:$PORT --log-file -
