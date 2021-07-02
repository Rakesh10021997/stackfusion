
web: gunicorn testapp.wsgi:application --log-file - 
python manage.py collectstatic --noinput
python manage.py migrate

