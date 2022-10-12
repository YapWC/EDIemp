from rest_framework import generics
from rest_framework.response import Response
from .serializers import EmployeeSerializer, DepartmentSerializer, Dep_EmpSerializer
from .models import Employee, Department, Dep_Emp

class EmployeeCreateApi(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeListApi(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDeleteApi(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#For Department
class DepartmentCreateApi(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentListApi(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDeleteApi(generics.DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

#For Department Employee
class Dep_EmpCreateApi(generics.CreateAPIView):
    queryset = Dep_Emp.objects.all()
    serializer_class = Dep_EmpSerializer

class Dep_EmpListApi(generics.ListAPIView):
    queryset = Dep_Emp.objects.all()
    serializer_class = Dep_EmpSerializer

class Dep_EmpUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Dep_Emp.objects.all()
    serializer_class = Dep_EmpSerializer

class Dep_EmpDeleteApi(generics.DestroyAPIView):
    queryset = Dep_Emp.objects.all()
    serializer_class = Dep_EmpSerializer
