from django.db import models

# Create your models here.

class user(models.Model):
    name=models.TextField(max_length=20)
    email=models.EmailField(max_length=30)