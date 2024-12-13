from .models import PaymentPlan, Payment
from django.utils import timezone

def process_monthly_payments():
    today = timezone.now().date()
    payment_plans = PaymentPlan.objects.filter(start_date__lte=today, end_date__gte=today)

    for plan in payment_plans:
        student = plan.student
        if student.balance >= plan.monthly_fee:
            student.balance -= plan.monthly_fee
            student.save()

            Payment.objects.create(student=student, amount=plan.monthly_fee, date=today)
        else:
            print(f"Insufficient balance for {student.name}")

