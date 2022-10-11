from rest_framework import  serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
                    'name','employee_ID','team',
                    'hourly_Rate', 'team_Leader',
                    'work','weekly_Work_Hour', 'Salary'
                    ]
