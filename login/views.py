from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def hello(request):

    return render(request, 'registration/login.html')

def hella(request):

    return render(request, 'registration/register.html')

@login_required
def hellobank(request):
    return render(request, 'bank.html')

def closeSession(request):
    logout(request)
    return redirect('login/')