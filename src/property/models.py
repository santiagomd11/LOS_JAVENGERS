from django.db import models
from calendarProperty.models import Calendar
class Property(models.Model):
    cost  = models.IntegerField()
    link = models.URLField()
    description = models.CharField(max_length=255)
    photos = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    calendarProperty = models.OneToOneField(Calendar, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class House(Property):
    squareMetters = models.IntegerField()
    stratus = models.IntegerField()
    roomsNumber = models.IntegerField()
    bathsNumber = models.IntegerField()
    location = models.CharField(max_length=255)

    
class Vehicle(Property):
    mileage = models.IntegerField()
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    motor = models.CharField(max_length=255)
# Create your models here.
