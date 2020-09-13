from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect

from authorization.forms import RegisterUserForm, LoginUserForm


def register_view(request):

    form = RegisterUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['login'],
                form.cleaned_data['email'],
                form.cleaned_data['password']
            )
            user.save()
            group = Group.objects.get(name='users')  # must be created before used, create through django admin
            user.groups.add(group)
            messages.add_message(request, messages.SUCCESS, f"Welcome {form.cleaned_data['login']}!!")

    return render(
        request,
        'authorization/register.html',
        context={'form': form}
    )


def login_view(request):

    form = LoginUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user_login = form.cleaned_data['login']
            user = authenticate(username=user_login, password=form.cleaned_data['password'])
            if user:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, f'Successfully logged in {user_login}!')

    return render (
        request,
        'authorization/login.html',
        context={'form': form}
    )


def logout_view(request):
    logout(request)

    return redirect(login_view)
