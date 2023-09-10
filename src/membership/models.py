from django.db import models

# Create your models here.
class Membership(models):
    class MemberShipType(models.IntegerChoices):
        FREE = 1, 'Free'
        BASIC = 2, 'Basic'
        GOLD = 3, 'Gold'
        PLATINUM = 4, 'Platinum'

    type = models.CharField(choices=MemberShipType.choices, max_length='15')
    cost = models.IntegerField()
    property_numbers = models.IntegerField()


    
