import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import CreatePetForm, EditPetForm
from petstagram.pets.models import Pet, Like


def pet_all(request):
    all_pets = Pet.objects.all()
    all_pets = sorted(all_pets, key=lambda x: x.id)
    context = {
        'pets': all_pets
    }

    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    comment_form = CommentForm(
        initial={'pet_pk': pk}
    )

    comments = Comment.objects.filter(pet=pet)

    is_liked = pet.like_set.filter(user_id=request.user.id)
    is_owner = pet.user == request.user

    context = {
        'pet': pet,
        'comments': comments,
        'comment_form': comment_form,
        'is_liked': is_liked,
        'is_owner': is_owner
    }

    return render(request, 'pets/pet_detail.html', context)


@login_required
def comment_pet(request, pk):
    form = CommentForm(
        request.POST,
    )

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

    return redirect('pet_details', pk)


@login_required
def pet_like(request, pk):
    pet = Pet.objects.get(pk=pk)

    user_like = pet.like_set.filter(user=request.user)

    if user_like:
        user_like.delete()

    else:
        Like(
            pet=pet,
            user=request.user,
        ).save()

    return redirect('pet_details', pk)


@login_required
def create_pet(request):
    if request.method == 'POST':
        form = CreatePetForm(request.POST, request.FILES)

        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('pet_all')

    else:
        form = CreatePetForm()

    context = {
        'form': form
    }
    return render(request, 'pets/pet_create.html', context)


@login_required
def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if pet.user != request.user:
        return redirect('pet_details', pk)

    old_image = pet.image.path

    if request.method == 'POST':
        form = EditPetForm(request.POST, request.FILES, instance=pet)

        if form.is_valid():
            if form.files:
                os.remove(old_image)

            form.save()
            return redirect('pet_details', pk)

    else:
        form = EditPetForm(instance=pet)

    context = {
        'form': form,
        'pet': pet
    }

    return render(request, 'pets/pet_edit.html', context)


@login_required
def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if pet.user != request.user:
        return redirect('pet_details', pk)

    if request.method == 'POST':
        pet.image.delete()
        pet.delete()
        return redirect('pet_all')

    context = {
        'pet': pet
    }

    return render(request, 'pets/pet_delete.html', context)
