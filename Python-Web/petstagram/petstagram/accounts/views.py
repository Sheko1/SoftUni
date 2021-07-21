import os

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from petstagram.accounts.forms import LoginForm, RegisterForm, UserProfileForm
from petstagram.accounts.models import UserProfile
from petstagram.pets.models import Pet


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('landing')

    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing')

    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('landing')


@login_required
def profile_details(request):
    profile = UserProfile.objects.get(pk=request.user.id)
    old_image = None

    if profile.profile_picture:
        old_image = profile.profile_picture.path

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            if old_image:
                os.remove(old_image)
            form.save()
            return redirect('profile details')

    else:
        form = UserProfileForm(instance=profile)

    pets = Pet.objects.filter(user=request.user)

    context = {
        'profile': profile,
        'form': form,
        'pets': pets,
    }

    return render(request, 'accounts/user_profile.html', context)
