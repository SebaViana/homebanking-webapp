from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField

import uuid


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    accountId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # to be modified