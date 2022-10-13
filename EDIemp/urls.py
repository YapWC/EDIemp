from django.urls import path, include
from django.contrib import admin

#Project/Main URLs
urlpatterns = [    
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
]