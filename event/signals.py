# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import EventDetails
from eventCalendar.models import Event


@receiver(post_save, sender=EventDetails)
def calendar_event(sender, instance, created, **kwargs):
    if created & instance.status2==True:
        # Subtract the amount from the associated product's stock
        Event.objects.create(title=instance.title, 
                             description=instance.description,
                               start_time=instance.start_date,
                                 end_time=instance.start_date)
        print('Event Added successfully')

        