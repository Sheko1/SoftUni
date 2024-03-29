from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


UserModel = get_user_model()


class Pet(models.Model):
    TYPE_CHOICE_DOG = 'Dog'
    TYPE_CHOICE_CAT = 'Cat'
    TYPE_CHOICE_PARROT = 'Parrot'

    TYPE_CHOICES = (
        (TYPE_CHOICE_DOG, 'Dog'),
        (TYPE_CHOICE_CAT, 'Cat'),
        (TYPE_CHOICE_PARROT, 'Parrot')
    )

    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
    )

    name = models.CharField(
        max_length=6
    )

    age = models.PositiveIntegerField(

    )

    description = models.TextField(

    )

    image = models.ImageField(
        upload_to='images',
        max_length=200
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
