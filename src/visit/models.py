from django.db import models
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext as _  # Importa gettext para traducción
class Visit(models.Model):
    class VisitType(models.IntegerChoices):
        HOUSE_TOUR = 0, _('HouseTour')
        TEST_DRIVE = 1,_('TestDrive')
    visitType = models.IntegerField(default=VisitType.HOUSE_TOUR, choices=VisitType.choices)
    dateTime  = models.DateTimeField()


# Create your models here.
