import os

from celery import Celery
from settings import REDIS_URL
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.conf.broker_url = REDIS_URL
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# from celery.schedules import crontab                # noqa: ERA001
#
# # Tasks                                             # noqa: ERA001
# app.conf.beat_schedule = {
#     'TASK_NAME': {                                  # noqa: ERA001
#         'task': 'APP.tasks.FUNCTION',               # noqa: ERA001
#         'schedule': crontab(hour=3, minute=0)       # noqa: ERA001
#     },
