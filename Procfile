web: gunicorn DatabaseBackupApp.wsgi --log-file -
main_worker: python manage.py celery worker --beat --scheduler django --loglevel=info