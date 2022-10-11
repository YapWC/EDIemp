from django.db import models
#import calculation
from django.utils.text import slugify 

# Create your models here.
class Employee(models.Model):
    name = models.TextField()
    employee_ID = models.TextField(unique=True)
    team = models.TextField(default='')
    hourly_Rate = models.IntegerField(default=0)
    team_Leader = models.TextField(default='')
    work = models.TextField(default='')
    weekly_Work_Hour = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def Salary(self):
        return int(self.weekly_Work_Hour)*int(self.hourly_Rate)*4