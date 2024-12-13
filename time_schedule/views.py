from rest_framework import viewsets
from .models import Student, PaymentPlan, Payment
from .serializers import StudentSerializer, PaymentPlanSerializer, PaymentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .utils import process_monthly_payments

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class PaymentPlanViewSet(viewsets.ModelViewSet):
    queryset = PaymentPlan.objects.all()
    serializer_class = PaymentPlanSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @action(detail=False, methods=['post'])
    def process_payments(self, request):
        process_monthly_payments()
        return Response({"status": "Payments processed successfully"})
