from django.shortcuts import render, HttpResponseRedirect, HttpResponse
import requests, json
from .secrets import api_token_paystack

# Create your views here.
from .paystack import Base

def pay_paystack(request):
    ac=Base()
    return HttpResponseRedirect(ac.make_payment("mitchelballzz@gmail.com", "4500"))


def hello(request):
    return HttpResponse('this is me')
