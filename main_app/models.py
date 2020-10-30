from django.db import models
from users.models import User
# Create your models here.


class TotalAmountManager(models.Manager):
    def get_queryset(self):
        amount = super(TotalAmountManager, self).get_queryset().all()
        total_amount=0
        for i in amount:
            total_amount = total_amount+i.amount
            print(total_amount, i.amount)
        return total_amount



class DepositModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount=models.IntegerField()
    date_in=models.DateTimeField( auto_now_add=True)

    totalamount=TotalAmountManager()
    objects = models.Manager()

    def __str__(self):
        return str(self.user)

    
    def return_amount(self):
        return self.amount

