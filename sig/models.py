from django.db import models

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    

class user_profile(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)