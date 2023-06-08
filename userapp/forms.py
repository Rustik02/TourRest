from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            'username':
                forms.TextInput(
                    attrs={
                        'placeholder': 'username'
                    }
                ),
            'email':
                forms.TextInput(
                    attrs={
                        'placeholder': 'password'
                    }
                ),

        }


class Authentication(AuthenticationForm):
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    username = forms.CharField(
        label='Email', widget=forms.EmailInput(attrs={'placeholder': 'username'}))

    class Meta:
        model = User
