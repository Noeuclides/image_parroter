import os
from image_parroter.settings import base
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_parroter.settings.local')

celery_app = Celery('image_parroter')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks(lambda : base.INSTALLED_APPS)
