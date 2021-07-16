from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    profile_picture = models.ImageField(
        upload_to='profiles',
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    is_complete = models.BooleanField(
        default=False
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
