web: gunicorn core.wsgi --log-file=-
release: python manage.py migrate
release: python manage.py createsuperuser