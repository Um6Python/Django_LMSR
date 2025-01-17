# market/admin.py
from django.contrib import admin
from .models import LMSRMarket, Transaction  # Import your models

# Register your models with the admin site
admin.site.register(LMSRMarket)
admin.site.register(Transaction)