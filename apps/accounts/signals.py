from typing import Any

from rest_framework.authtoken.models import Token

from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import User, Profile


@receiver(post_save, sender=User, dispatch_uid="create_update_profile")
def create_or_update_user_profile(sender: Any, instance: Any, created: bool, **kwargs: Any) -> None:
    if created:
        Profile.objects.create(user=instance)
        Token.objects.create(user=instance)
    instance.profile.save()
