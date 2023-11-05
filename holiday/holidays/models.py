from django.db import models

# Create your models here.
class DayHoliday(models.Model):
    date = models.CharField(max_length=50)
    celebrate = models.CharField(max_length=200)
