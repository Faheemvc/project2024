# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import user, user_profile

@receiver(post_save, sender=user)
def update_user(sender, instance, created, **kwargs):
    if created:
        # Subtract the amount from the associated product's stock
        print('User created')
        print(instance.first_name)
        user_profile.objects.create(email=instance.email, password=instance.password)
        