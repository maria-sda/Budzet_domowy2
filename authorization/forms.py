from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterUserForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    email = forms.EmailField()

    def clean_login(self):
        login = self.cleaned_data['login']
        if User.objects.filter(username=login).exists():
            raise ValidationError('User with this username already exists.')
        return login


class LoginUserForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
