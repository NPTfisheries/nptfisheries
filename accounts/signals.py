#accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, UserProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        #employer = instance.employer
        #work_phone = instance.work_phone
        #mobile_phone = instance.mobile_phone
        #email_updates = instance.email_updates

        UserProfile.objects.create(user=instance)