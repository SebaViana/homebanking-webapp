from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default = 100)