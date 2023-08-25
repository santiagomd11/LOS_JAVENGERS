from django.db import models

# Create your models here.

class User(models.Model):
    user_name  = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
