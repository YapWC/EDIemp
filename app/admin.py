from django.contrib import admin

from .models import Employee, Dep_Emp, Department

#Register the models into
#admin page
admin.site.register(Employee)
admin.site.register(Dep_Emp)
admin.site.register(Department)