from django.db import models
# Create your models here.
class Employee(models.Model):
    name = models.TextField()
    employee_ID = models.TextField(unique=True)
    team = models.TextField(default='Not Mentioned')
    hourly_Rate = models.TextField(default='Not Mentioned')
    team_leader = models.TextField(default='Not Mentioned')
    work = models.TextField(default='Not Mentioned')

    #created_at = models.DateTimeField(auto_now=True)