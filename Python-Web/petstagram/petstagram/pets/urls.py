from django.urls import path

from petstagram.pets.views import pet_all, pet_details, pet_like

urlpatterns = [
    path('', pet_all, name='pet_all'),
    path('details/<int:pk>', pet_details, name='pet_details'),
    path('like/<int:pk>', pet_like, name='pet_like'),
]
