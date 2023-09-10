from django.db import models

# Create your models here.


class UserAuthentication(models):
    legalDocumentNumber = models.CharField(max_length=10)
    legalDocumentPhoto = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    userPhoto = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)