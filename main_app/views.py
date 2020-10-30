from urllib.parse import parse_qs
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from users.models import User
from .paystack import Base
from .forms import DepositForm
from .models import DepositModel
import urllib.parse as urlparse
import json
# Create your views here.

def home(request):
    return render(request, 'home.html')

    

def dashboard(request):
    amount=DepositModel.objects.filter(user=request.user)
    sum_amount = DepositModel.totalamount.all()

    """amount = summation of deposits - summation of all withdrawls"""
    return render(request, 'dashboard.html', context={"amount": sum_amount})


def _dashboard(request):

    amount = DepositModel.objects.filter(user=request.user)
    sum_amount = DepositModel.totalamount.all()
   
    """amount = summation of deposits - summation of all withdrawls"""


    url = request.get_raw_uri()
    print(url)
    parsed = urlparse.urlparse(url)
    txref = parse_qs(parsed.query)['trxref']
    reference = parse_qs(parsed.query)['reference']
    print(txref, reference)

    deposit = Base()
    payment_details=deposit.confirm_payment(" ".join(txref))
    #print(payment_details)

    for keys, values in dict(payment_details).items():
        #print(keys)
     
        if "data" in keys:
            for key, value in values.items():
                if "amount" in key:
                    print(value)
                    deposit_amount = DepositModel()
                    deposit_amount.user=request.user
                    deposit_amount.amount=value/100
                    print(deposit_amount.amount)
                    deposit_amount.save()
                    break
    return render(request, 'payment_successful_dashboard.html', context={"amount": sum_amount})



def payment(request):
    if request.method == "POST":
        form=DepositForm(request.POST)
        if form.is_valid():
            amount=str(int(form.cleaned_data['amount']) * 100)
            deposit=Base()
            
            return HttpResponseRedirect(deposit.make_payment(str(request.user.email), str(amount)))
    else:
        form = DepositForm()

    return render(request, 'payment.html', context={"form":form})
