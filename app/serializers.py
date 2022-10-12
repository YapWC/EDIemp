from rest_framework import  serializers
from .models import Employee, Department

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
                    'name','employee_ID',
                    'team','hourly_Rate'
                    ]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
                    'employee','Employee_name','team_Leader',
                    'work','weekly_Work_Hour','Salary'
                    ]