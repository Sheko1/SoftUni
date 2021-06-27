from django.urls import path

from petstagram.pets.views import pet_all, pet_details, pet_like, create_pet, edit_pet, delete_pet

urlpatterns = [
    path('', pet_all, name='pet_all'),
    path('details/<int:pk>', pet_details, name='pet_details'),
    path('like/<int:pk>', pet_like, name='pet_like'),
    path('create/', create_pet, name='create_pet'),
    path('edit/<int:pk>', edit_pet, name='edit_pet'),
    path('delete/<int:pk>', delete_pet, name='delete_pet'),
]
