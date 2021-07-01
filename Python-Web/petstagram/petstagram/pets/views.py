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
    if request.method == 'POST':
        form = CommentForm(
            request.POST,
            initial={'pet_pk': pk}
        )

        if form.is_valid():
            form.save()
            return redirect('pet_details', pk)

    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    comment_form = CommentForm(
        initial={'pet_pk': pk}
    )

    comments = Comment.objects.filter(pet=pet)

    context = {
        'pet': pet,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'pets/pet_detail.html', context)


def pet_like(request, pk):
    pet = Pet.objects.get(pk=pk)
    Like(pet=pet).save()

    return redirect('pet_details', pk)


def create_pet(request):
    if request.method == 'POST':
        form = CreatePetForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('pet_all')

    else:
        form = CreatePetForm()

    context = {
        'form': form
    }
    return render(request, 'pets/pet_create.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditPetForm(request.POST, instance=pet)

        if form.is_valid():
            form.save()
            return redirect('pet_details', pk)

    else:
        form = EditPetForm(instance=pet)

    context = {
        'form': form,
        'pet': pet
    }

    return render(request, 'pets/pet_edit.html', context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == 'POST':
        pet.delete()
        return redirect('pet_all')

    context = {
        'pet': pet
    }

    return render(request, 'pets/pet_delete.html', context)
