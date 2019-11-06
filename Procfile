web: gunicorn DatabaseBackupApp.wsgi --log-file -
worker: celery worker --beat --scheduler django --loglevel=info