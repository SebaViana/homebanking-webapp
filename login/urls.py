from django import views
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from login.views import ResetPasswordView

urlpatterns = [
    path('login/', views.hello, name='login'),
    path('register/', views.hella, name='register'),
    #path('password-reset/', views.passwordReset, name='password-reset'),
    path('', views.hellobank, name='onlinebanking'),
    path('', views.closeSession, name='logout'),
    path('change-password/', views.changePassword, name = 'change-password'),
    path('transfer', views.transfer, name="transfer"),

    path('password-reset/', ResetPasswordView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password-reset-confirm.html'),
        name='password-reset-confirm'),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='registration/password-reset-complete.html'),
        name='password-reset-complete'),
    
    path('customer-supoprt', views.customerSupport, name='customer-support'),
]