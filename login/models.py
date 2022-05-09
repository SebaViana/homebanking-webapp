from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.forms import DecimalField
from djmoney.models.fields import MoneyField, Money

import uuid
import random

def generateAccountId():
    return str(random.randint(100000, 999999))

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = MoneyField(max_digits=14, decimal_places=2, default=Money(1000, "USD"))
    accountId = models.CharField(primary_key=True, default=generateAccountId, editable=False, max_length=6) # to be modified

class Transaction(models.Model):
    to_account = models.CharField(max_length=6)
    amount = DecimalField(max_digits=5, decimal_places=2)

    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.amount)
