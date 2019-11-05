web: gunicorn DatabaseBackupApp.wsgi --log-file -
worker: python manage.py celery worker --beat --scheduler django --loglevel=info