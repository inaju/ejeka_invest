from django.contrib import admin
from .models import DepositModel
from users.models import User
# Register your models here.

class DepositAdmin(admin.ModelAdmin):
    #list_display = ('first_name',)
    readonly_fields=['amount', 'date_in',]
    


admin.site.register(DepositModel, DepositAdmin)
