from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from login.models import Transaction

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Enter a username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter a password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter your password'

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class TransactionForm(forms.ModelForm):
    to_account = forms.CharField(max_length=6)
    amount = forms.DecimalField(max_digits=5)
    
    class Meta:
        model=Transaction
        fields = '__all__'