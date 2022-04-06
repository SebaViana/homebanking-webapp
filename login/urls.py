from django import views
from django.urls import include, path
from . import views

urlpatterns = [
    path('login/', views.hello, name='login'),
    path('register/', views.hella, name='register'),
    path('', views.hellobank),
    path('', views.closeSession, name='logout')
]