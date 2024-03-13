# Generated by Django 4.2.7 on 2024-03-13 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_eventdetails_delete_appointment_delete_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdetails',
            name='end_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='eventdetails',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
