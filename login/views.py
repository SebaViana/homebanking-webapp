from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from .models import Wallet

def hello(request):
    if request.user.is_authenticated:
        return redirect('onlinebanking')
    return render(request, 'registration/login.html')

def hella(request):
    if request.user.is_authenticated:
        return redirect('onlinebanking')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()            
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form':form})

@login_required
def hellobank(request):
    
    try:
        user = Wallet.objects.get(user=request.user)
    except Wallet.DoesNotExist:
        instance = Wallet(user = request.user, balance = 0)
        instance.save()
        user = Wallet.objects.get(user=request.user)
    
    return render(request, 'bank.html', {"balance":user.balance})

def closeSession(request):
    logout(request)
    return redirect('login/')