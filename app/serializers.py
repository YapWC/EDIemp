from rest_framework import  serializers
from .models import Employee, Department, Dep_Emp

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
                    'name','employee_ID',
                    'hourly_Rate'
                    ]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['create_department']

class Dep_EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dep_Emp
        fields = [
                    'Name','Employee_team','team_Leader',
                    'work','weekly_Work_Hour','Salary'
                    ]