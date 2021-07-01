from django.shortcuts import render, redirect

# Create your views here.
from core.profile_utils import get_profile
from notes.notes_app.models import Note


def profile_page(request):
    profile = get_profile()
    notes = Note.objects.all()

    context = {
        'profile': profile,
        'notes': len(notes)
    }

    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    notes = Note.objects.all()

    if profile:
        profile.delete()
        notes.delete()

    return redirect('home page')
