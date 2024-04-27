from .models import Employee
from rest_framework import viewsets, permissions 
from .serializer import EmployeeSerializer

class ApiViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]