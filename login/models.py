from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField, Money

import uuid
import random

def generateAccountId():
    return str(random.randint(100000, 999999))

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = MoneyField(max_digits=14, decimal_places=2, default=Money(1000, "USD"))
    accountId = models.CharField(primary_key=True, default=generateAccountId, editable=False, max_length=6) # to be modified