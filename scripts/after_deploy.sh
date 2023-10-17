source /var/app/venv/*/bin/activate
python manage.py collectstatic
python manage.py migrate --noinput
python manage.py superuser