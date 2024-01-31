

from django.db import models

# Create your models here.
from django.urls import reverse


class Month(models.Model):
    number_month = models.IntegerField(unique=True)
    name_month = models.CharField(max_length=255, unique=True)
    count_day = models.IntegerField()
    url_name = models.SlugField(db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('month', kwargs={'slug_month': self.url_name})



class Day(models.Model):
    number_day = models.IntegerField(unique=True)
    url_name = models.SlugField(unique=True)

    # 'month/<slug:slug_month>/<slug:slug_day>/'
    def get_absolute_url(self):
        return reverse('month', kwargs={'slug_month': Month.url_name,
                                        'slug_day': self.url_name})

class Holiday(models.Model):
    name = models.CharField(max_length=255)
    url_name = models.SlugField(unique=True)
    international = models.BooleanField(default=False)
    worldwide = models.BooleanField(default=False)
    ordinary_holiday = models.BooleanField(default=False)
    date_holiday = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('day', kwargs={'slug_holiday': self.url_name})