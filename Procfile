
web: gunicorn testapp.wsgi:application --log-file - 
python manage.py collectstatic --noinput
release: python manage.py migrate --no-input




