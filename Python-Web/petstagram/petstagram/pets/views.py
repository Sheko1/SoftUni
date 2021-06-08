from django.shortcuts import render, redirect

# Create your views here.
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
    context = {
        'pet': pet
    }
    return render(request, 'pets/pet_detail.html', context)


def pet_like(request, pk):
    pet = Pet.objects.get(pk=pk)
    Like(pet=pet).save()

    return redirect('pet_details', pk)
