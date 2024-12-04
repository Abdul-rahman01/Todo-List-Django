from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


INPUT_CLASSES = 'full'


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': INPUT_CLASSES
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': INPUT_CLASSES
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': INPUT_CLASSES
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email Address',
        'class': INPUT_CLASSES
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': INPUT_CLASSES
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password',
        'class': INPUT_CLASSES
    }))