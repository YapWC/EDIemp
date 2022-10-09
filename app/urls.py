from django.urls import path
from .views import EmployeeCreateApi, EmployeeListApi, EmployeeUpdateApi, EmployeeDeleteApi
urlpatterns = [
    path('employee/create',EmployeeCreateApi.as_view()),
    path('employee/list',EmployeeListApi.as_view()),
    path('employee/<int:pk>',EmployeeUpdateApi.as_view()),
     path('employee/<int:pk>/delete',EmployeeDeleteApi.as_view()),
]