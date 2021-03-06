
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DatabaseBackupApp.settings')

from django.conf import settings
redis_url='redis://:ij48D89BGX4F1Asz3UoaVrcRJ4DxqjTs@redis-10487.c124.us-central1-1.gce.cloud.redislabs.com:10487'
app = Celery('DatabaseBackupApp', broker=redis_url, result_backend=redis_url)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://localhost:6379/0'

#app.conf.broker_url = 'redis://:ij48D89BGX4F1Asz3UoaVrcRJ4DxqjTs@redis-10487.c124.us-central1-1.gce.cloud.redislabs.com:10487/1'
'''app.conf.update(BROKER_URL=os.environ['redis://redis-10487.c124.us-central1-1.gce.cloud.redislabs.com:10487'],
                CELERY_RESULT_BACKEND=os.environ['redis://redis-10487.c124.us-central1-1.gce.cloud.redislabs.com:10487'])'''
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(['SystemsApp']) 
#app.autodiscover_tasks() 
