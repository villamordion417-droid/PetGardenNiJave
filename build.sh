#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Create superuser if it doesn't exist (Smarter version)
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = '$DJANGO_SUPERUSER_USERNAME'
email = '$DJANGO_SUPERUSER_EMAIL'
password = '$DJANGO_SUPERUSER_PASSWORD'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superuser "{username}" created.')
else:
    print(f'Superuser "{username}" already exists. Skipping.')
EOF