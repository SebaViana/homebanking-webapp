from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
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
        instance = Wallet(user = request.user)
        instance.save()
        user = Wallet.objects.get(user=request.user)
    
    return render(request, 'bank.html', {"balance":user.balance})

def closeSession(request):
    logout(request)
    return redirect('login/')

def redirectHome(request):
    return redirect('onlinebanking')

def passwordReset(request):
    return render(request, 'registration/password-reset.html')

def changePassword(request):
    if request.method == 'POST':
        PasswordChange_form = PasswordChangeForm(request.user, request.POST)
        if PasswordChange_form.is_valid():
            user = PasswordChange_form.save()
            update_session_auth_hash(request, user)
            return redirect('onlinebanking')
    else:
        PasswordChange_form = PasswordChangeForm(request.user)

    context= {
    'PasswordChange_form': PasswordChange_form,
    'date_joined': request.user.date_joined,
    'last_login': request.user.last_login,
    'first_name': request.user.first_name,
    'last_name': request.user.last_name,
    'accountId': Wallet.objects.get(user=request.user).accountId
    }

    return render(request, 'registration/change-password.html', context)

def transfer(request):
    user = Wallet.objects.get(user=request.user)
    return render(request, 'transfer.html', {"balance":user.balance})