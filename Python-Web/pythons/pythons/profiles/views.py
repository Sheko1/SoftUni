from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from pythons.profiles.forms import ProfileForm
from pythons.profiles.models import Profile


@login_required
def view_profile(req):
    profile = Profile.objects.get(pk=req.user.id)
    profile.username = req.user.username

    if not profile.is_complete:
        return edit_profile(req)

    context = {
        'profile': profile
    }

    return render(req, 'profile/view_profile.html', context)


@login_required
def edit_profile(req):
    profile = Profile.objects.get(pk=req.user.id)

    if req.method == 'POST':
        form = ProfileForm(req.POST, req.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form
    }

    return render(req, 'auth/../../templates/profile/edit_profile.html', context)
