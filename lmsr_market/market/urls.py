# market/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.market_view, name='market_view'),
    path('buy/', views.buy_shares, name='buy_shares'),
    path('sell/', views.sell_shares, name='sell_shares'),
    path('signup/', views.signup, name='signup'),
]
