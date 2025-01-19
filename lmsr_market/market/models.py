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
    
class Market(models.Model):
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    image_url = models.URLField(blank=True, null=True)  # Add an image URL field
    outcomes = models.JSONField(default=list)  # Add a JSON field for outcomes
    def __str__(self):
        return self.question
    

    
class Prediction(models.Model):
    STOCK_CHOICES = [
        ('stock1', 'Canada: 51st state'),
        ('stock2', 'No'),
        ('stock3', 'Trump will die before, He is too old')
    ]
    
    stock = models.CharField(max_length=20, choices=STOCK_CHOICES)
    shares = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_stock_display()} - {self.shares} shares"
    

