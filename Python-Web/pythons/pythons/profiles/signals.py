from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from pythons.profiles.models import Profile


@receiver(post_save, sender=User)
def user_created(**kwargs):
    if kwargs['created']:
        profile = Profile(
            user=kwargs['instance'],
        )
        profile.save()


@receiver(pre_save, sender=Profile)
def check_is_complete(**kwargs):
    if kwargs['instance'].profile_picture and kwargs['instance'].description and kwargs['instance'].description:
        kwargs['instance'].is_complete = True
