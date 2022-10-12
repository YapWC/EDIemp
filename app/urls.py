from django.urls import path
from .views import (
                    EmployeeCreateApi, EmployeeListApi, EmployeeUpdateApi, EmployeeDeleteApi,
                    DepartmentCreateApi, DepartmentListApi, DepartmentUpdateApi, DepartmentDeleteApi
                    )


urlpatterns = [
    path('employee/create',EmployeeCreateApi.as_view()),
    path('employee/list',EmployeeListApi.as_view()),
    path('employee/<int:pk>',EmployeeUpdateApi.as_view()),
    path('employee/<int:pk>/delete',EmployeeDeleteApi.as_view()),

    path('team/create',DepartmentCreateApi.as_view()),
    path('team/list',DepartmentListApi.as_view()),
    path('team/<int:pk>',DepartmentUpdateApi.as_view()),
    path('team/<int:pk>/delete',DepartmentDeleteApi.as_view()),
]