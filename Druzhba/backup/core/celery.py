import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# from celery.schedules import crontab
#
# # Tasks
# app.conf.beat_schedule = {
#     'TASK_NAME': {
#         'task': 'APP.tasks.FUNCTION',
#         'schedule': crontab(hour=3, minute=0)
#     },
# }
