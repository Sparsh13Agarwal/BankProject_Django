from django.contrib import admin
from .models import Customer,Transaction,Credential,contact_us


class AdminCustomer(admin.ModelAdmin):
    list_display = ['customer_id','account_number','first_name','last_name','resident_address','office_address','phone_number','email']

class AdminTransaction(admin.ModelAdmin):
    list_display = ['customer_id','transaction_id','transaction_account','transaction_amount']

class AdminCred(admin.ModelAdmin):
    list_display = ['customer_id','password']

class AdminMessage(admin.ModelAdmin):
    list_display = ['name','email','message']

admin.site.register(Customer,AdminCustomer)
admin.site.register(Transaction,AdminTransaction)
admin.site.register(Credential,AdminCred)
admin.site.register(contact_us,AdminMessage)