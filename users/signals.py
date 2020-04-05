# To avoid creating profiles again and again as admin

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender = User ) # When user send a signal of post_save recieve by reciever
def create_profile(sender, instance, created, **kwargs):
    # if user was created create profile
    if created:
        Profile.objects.create(user = instance)


@receiver(post_save, sender = User ) # When user send a signal of post_save recieve by reciever
def save_profile(sender, instance, **kwargs): # **kwargs accepts any other additional arg at the end
    instance.profile.save()

# After this go to users app > apps.py 