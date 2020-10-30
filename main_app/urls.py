
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls import url
#from users import urls

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('payment/', views.payment, name='payment'),
    re_path(r'^_dashboard/',views._dashboard, name='_dashboard'),
]
