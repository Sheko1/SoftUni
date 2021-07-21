from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


UserModel = get_user_model()


class UserProfile(models.Model):
    profile_picture = models.ImageField(
        upload_to='profiles',
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
