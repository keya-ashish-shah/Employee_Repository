from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:pk>/',views.employee_detail,name='employee_detail'),

]