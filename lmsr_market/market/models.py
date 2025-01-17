from django.db import models
from django.contrib.auth.models import User


# Create your models here.

    
# market/models.py
from django.db import models

class LMSRMarket(models.Model):
    name = models.CharField(max_length=100)
    b = models.FloatField()
    q = models.JSONField()  # Assuming q is a JSON field

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    market = models.ForeignKey(LMSRMarket, on_delete=models.CASCADE)
    outcome = models.CharField(max_length=100)
    shares = models.IntegerField()
    cost = models.FloatField()
    transaction_type = models.CharField(max_length=4, choices=[('buy', 'Buy'), ('sell', 'Sell')])

    def __str__(self):
        return f"{self.user.username} - {self.market.name} - {self.outcome} - {self.transaction_type}"
    
