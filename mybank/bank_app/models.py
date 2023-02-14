
from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.CharField(max_length=10,primary_key=True)
    account_number = models.CharField(max_length=20,unique=True)
    first_name = models.CharField(max_length=20,blank=False)
    middle_name = models.CharField(max_length=20,blank=True)
    last_name = models.CharField(max_length=20,blank=False) 
    resident_address = models.CharField(max_length=300,blank=False)
    office_address = models.CharField(max_length=300,blank=False)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    Balance = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.customer_id

class Transaction(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=20,primary_key=True)
    transaction_amount = models.CharField(max_length=20) #changed type
    transaction_account = models.CharField(max_length=20)

class Credential(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    blocked = models.BooleanField(default=False)

class contact_us(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)