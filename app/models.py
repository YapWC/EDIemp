from django.db import models

# Creating Employee Entries Here
class Employee(models.Model):
    name = models.TextField(default='')
    employee_ID = models.IntegerField(default='',unique=True)
    hourly_Rate = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

# Creating Department Entries Here
class Department(models.Model):
    create_department = models.TextField(default='')

    def __str__(self):
        return self.create_department

# Creating Employee Entries Based on Their Respective Department
class Dep_Emp(models.Model):
    work_arrangement = (
                            ('Full Time','Full Time'),
                            ('Part Time','Part Time')
                        )
    
    leader_position = (
                            ('TRUE','YES'),
                            ('FALSE','NO')
                        )

    currency = 'EUR'

    department = models.ForeignKey(Department, on_delete=models.CASCADE,default='')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default='')
    team_Leader = models.TextField(choices=leader_position,default='')
    work = models.TextField(choices=work_arrangement,default='')
    weekly_Work_Hour = models.IntegerField(default=0)

    def Name(self):
        return self.employee.name

    def Employee_team(self):
        return self.department.create_department

    def status(self):
        return self.team_Leader

    def Salary(self):
        if self.team_Leader == 'TRUE':
            return self.currency+' '+str(int(self.weekly_Work_Hour)*int(self.employee.hourly_Rate)*4*110/100)
        else:
            return self.currency+' '+str(int(self.weekly_Work_Hour)*int(self.employee.hourly_Rate)*4)

    def __str__(self):
        return self.department.create_department+'_'+self.employee.name