import ast

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Partner(models.Model):
    """Base class for Partner."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='+',
    )
    address = models.CharField(
        max_length=300,
    )

    def __str__(self):
        return self.user.get_full_name()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Partner.objects.create(user=instance)
