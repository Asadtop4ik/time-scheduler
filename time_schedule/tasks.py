
from celery import shared_task
from .utils import process_monthly_payments

@shared_task
def process_monthly_payments_task():
    process_monthly_payments()
