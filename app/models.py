from django.db import models
#import calculation

# Create your models here.
class Employee(models.Model):
    name = models.TextField()
    employee_ID = models.TextField(unique=True)
    team = models.TextField(default='')
    hourly_Rate = models.IntegerField(default='')
    
    def __str__(self):
        return self.name

class Department(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    team_Leader = models.TextField(default='')
    work = models.TextField(default='')
    weekly_Work_Hour = models.IntegerField(default=0)

    def Employee_name(self):
        return self.employee.name

    def Salary(self):
        return int(self.weekly_Work_Hour)*int(self.employee.hourly_Rate)*4

    def __str__(self):
        return self.employee.team