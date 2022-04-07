from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

def hello(request):

    return render(request, 'registration/login.html')

def hella(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form':form})

@login_required
def hellobank(request):
    return render(request, 'bank.html')

def closeSession(request):
    logout(request)
    return redirect('login/')