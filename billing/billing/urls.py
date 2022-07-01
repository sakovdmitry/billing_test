from django.contrib import admin
from django.urls import path, include
from billingapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('billingapp.urls')),
    path('', views.simple_upload)
]
