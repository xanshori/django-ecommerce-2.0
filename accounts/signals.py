from django.db.models.signals import post_save
from .models import Account,Profile
from django.dispatch import receiver

@receiver(post_save, sender=Account)
def saveProfile(sender,instance,created,**kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            first_name=user.first_name,
            last_name=user.last_name,
            phone_number=user.phone_number,
        )
        profile.save()