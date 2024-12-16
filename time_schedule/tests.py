from django.utils import timezone  # Correct import for Django's timezone utilities
from django.test import TestCase
from time_schedule.models import Student, PaymentPlan
from time_schedule.utils import process_monthly_payments

class PaymentProcessingTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name="Test Student", balance=1000)
        self.plan = PaymentPlan.objects.create(
            student=self.student,
            monthly_fee=100,
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timezone.timedelta(days=30),
        )

    def test_process_monthly_payments(self):
        process_monthly_payments()
        self.student.refresh_from_db()
        self.assertEqual(self.student.balance, 900)  # Check balance deduction
        self.assertEqual(self.student.payment_set.count(), 1)  # Check payment record
