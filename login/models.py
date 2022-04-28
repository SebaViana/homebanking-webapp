from django.db import models
from django.contrib.auth.models import User
import uuid

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default = 100)
    accountId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # to be modified