from django.db import models
from django.utils import timezone


# Create your models here.
class Measurement(models.Model):
    value = models.DecimalField(max_digits=3, decimal_places=0)
    measured_date = models.DateField(default=timezone.now)
    notes = models.TextField()
