from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext as _  # Importa gettext para traducción
from visit.models import Visit

class Calendar(models.Model):
    class CalendarType(models.IntegerChoices):
        CALENDAR_USER = 0, _('CalendarUser')
        CALENDAR_PROPERTY = 1, _('CalendarProperty')
    
    calendarType = models.IntegerField(
        default=CalendarType.CALENDAR_USER,
        choices=CalendarType.choices
    )
    visits = models.ManyToManyField(Visit)  # Cambio "Visits" a minúscula para seguir convenciones de nombres

# Create your models here.
