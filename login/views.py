from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
import decimal
from .forms import RegisterForm, TransactionForm
from .models import Wallet
from djmoney.models.fields import MoneyField, Money
import logging

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

logging.basicConfig(level=logging.NOTSET)

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

""" def transfer(request):
    user = Wallet.objects.get(user=request.user)
    return render(request, 'transfer.html', {"balance":user.balance}) """

def transfer(request):
    user = Wallet.objects.get(user=request.user)
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            sender = Wallet.objects.get(user=request.user)
            if sender.balance.amount > Money(request.POST.get('amount')).amount:
                trans = form.save()
                trans.account_owner = request.user
                sender.balance.amount -= int(request.POST.get('amount'))
                sender.save()
                receiver = Wallet.objects.get(accountId=request.POST.get('to_account'))
                receiver.balance.amount += int(request.POST.get('amount'))
                receiver.save()
                return redirect ('transfer')

    else:
        form = TransactionForm
    context= {
    'TransactionForm_form': form,
    "balance":user.balance
    }
    return render(request, "transfer.html", context)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/password-reset.html'
    email_template_name = 'password_reset/password_reset_email.html'
    subject_template_name = 'password_reset/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                    "if an account exists with the email you entered. You should receive them shortly." \
                    " If you don't receive an email, " \
                    "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('onlinebanking')