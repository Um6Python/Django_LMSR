from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import LMSRMarket, Transaction
from .forms import BuySharesForm, SellSharesForm, SignUpForm
import math


@login_required
def market_view(request):
    market = LMSRMarket.objects.first()
    if market is None:
        # Render a template indicating no market is available
        return render(request, 'market/no_market.html')  
    
    prices = calculate_prices(market)
    user_transactions = Transaction.objects.filter(user=request.user, market=market)
    context = {
        'market': market,
        'prices': prices,
        'user_transactions': user_transactions,
    }
    return render(request, 'market/market.html', context)

def calculate_prices(market):
    if market is None or market.q is None:
        return {}
    exp_q = {outcome: math.exp(market.q[outcome] / market.b) for outcome in market.q}
    total = sum(exp_q.values())
    return {outcome: exp_q[outcome] / total for outcome in market.q}



@login_required
def profile(request):
    return render(request, 'registration/profile.html')

@login_required
def buy_shares(request):
    market = LMSRMarket.objects.first()
    if request.method == 'POST':
        form = BuySharesForm(request.POST)
        if form.is_valid():
            outcome = form.cleaned_data['outcome']
            shares = form.cleaned_data['shares']
            cost = buy_shares_logic(market, outcome, shares)
            Transaction.objects.create(user=request.user, market=market, outcome=outcome, shares=shares, cost=cost, transaction_type='buy')
            return redirect('market_view')
    else:
        form = BuySharesForm()
    return render(request, 'market/buy_shares.html', {'form': form})

@login_required
def sell_shares(request):
    market = LMSRMarket.objects.first()
    if request.method == 'POST':
        form = SellSharesForm(request.POST)
        if form.is_valid():
            outcome = form.cleaned_data['outcome']
            shares = form.cleaned_data['shares']
            refund = sell_shares_logic(market, outcome, shares)
            Transaction.objects.create(user=request.user, market=market, outcome=outcome, shares=-shares, cost=-refund, transaction_type='sell')
            return redirect('market_view')
    else:
        form = SellSharesForm()
    return render(request, 'market/sell_shares.html', {'form': form})

def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('market_view')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def buy_shares_logic(market, outcome, delta_q):
    current_cost = cost_function(market)
    market.q[outcome] += delta_q
    new_cost = cost_function(market)
    market.save()
    return new_cost - current_cost

def sell_shares_logic(market, outcome, delta_q):
    current_cost = cost_function(market)
    market.q[outcome] -= delta_q
    new_cost = cost_function(market)
    market.save()
    return current_cost - new_cost

def cost_function(market):
    total_exp_q = sum(math.exp(q_i / market.b) for q_i in market.q.values())
    return market.b * math.log(total_exp_q)