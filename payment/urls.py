from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    #path('', views.hello),
    path('', views.pay_paystack, name='paystack'),


]
