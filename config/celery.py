from celery.schedules import crontab
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.broker_connection_retry_on_startup = True

app.conf.beat_schedule = {
    'monthly-payment-task': {
        'task': 'time_schedule.tasks.process_monthly_payments_task',
        'schedule': crontab(day_of_month=1, hour=0, minute=0),
    },
}