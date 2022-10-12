from django.contrib import admin

from .models import Employee, Dep_Emp, Department

admin.site.register(Employee)
admin.site.register(Dep_Emp)
admin.site.register(Department)