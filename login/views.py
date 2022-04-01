from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def hello(request):

    return render(request, 'registration/login.html')

def hella(request):

    return render(request, 'registration/register.html')

@login_required
def hellobank(request):
    return render(request, 'bank.html')