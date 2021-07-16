from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
from pythons.pythons_auth.forms import LoginForm


def login_view(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('index')

    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(req, 'auth/login.html', context)


def logout_view(req):
    logout(req)
    return redirect('index')


def register_view(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {
        'form': form
    }

    return render(req, 'auth/register.html', context)
