from django.db.models.signals import post_save
from .models import Account,Profile
from django.dispatch import receiver

# @receiver(post_save, sender=Account)
# def saveProfile(sender,instance,created,**kwargs):
