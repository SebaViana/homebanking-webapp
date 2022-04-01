from django import views
from django.urls import include, path
from . import views

urlpatterns = [
    path('login/', views.hello),
    path('register/', views.hella),
    path('bank/', views.hellobank),
]