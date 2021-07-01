from django.shortcuts import render, redirect

# Create your views here.
from core.profile_utils import get_profile
from notes.notes_app.forms import NoteCreateForm, NoteEditForm, NoteDeleteForm
from notes.notes_app.models import Note
from notes.profile_app.forms import ProfileForm


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = ProfileForm()

    context = {
        'form': form
    }

    return render(request, 'home-no-profile.html', context)


def home_page(request):
    profile = get_profile()

    if not profile:
        return create_profile(request)

    notes = Note.objects.all()

    context = {
        'notes': notes
    }

    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = NoteCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = NoteCreateForm()

    context = {
        'form': form
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = NoteEditForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = NoteEditForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    form = NoteDeleteForm(instance=note)

    if request.method == 'POST':
        note.delete()
        return redirect('home page')

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note
    }

    return render(request, 'note-details.html', context)
