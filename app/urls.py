from django.urls import path
from .views import (
                    EmployeeCreateApi, EmployeeListApi, EmployeeUpdateApi, EmployeeDeleteApi,
                    DepartmentCreateApi, DepartmentListApi, DepartmentUpdateApi, DepartmentDeleteApi,
                    Dep_EmpCreateApi, Dep_EmpListApi, Dep_EmpUpdateApi, Dep_EmpDeleteApi
                    )


urlpatterns = [
    path('employee/create',EmployeeCreateApi.as_view()),
    path('employee/list',EmployeeListApi.as_view()),
    path('employee/<int:pk>',EmployeeUpdateApi.as_view()),
    path('employee/<int:pk>/delete',EmployeeDeleteApi.as_view()),

    path('team/emplyoee/create',Dep_EmpCreateApi.as_view()),
    path('team/employee/list',Dep_EmpListApi.as_view()),
    path('team/employee/<int:pk>',Dep_EmpUpdateApi.as_view()),
    path('team/employee/<int:pk>/delete',Dep_EmpDeleteApi.as_view()),

    path('department/create',DepartmentCreateApi.as_view()),
    path('department/list',DepartmentListApi.as_view()),
    path('department/<int:pk>',DepartmentUpdateApi.as_view()),
    path('department/<int:pk>/delete',DepartmentDeleteApi.as_view()),
]