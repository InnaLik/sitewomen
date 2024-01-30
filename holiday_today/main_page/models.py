from django.db import models

# Create your models here.
class Month(models.Model):
    number_month = models.IntegerField(unique=True)
    name_month = models.CharField(max_length=255, unique=True)
    count_day = models.IntegerField()
    url_name = models.SlugField(db_index=True, unique=True)


class Day(models.Model):
    number_day = models.IntegerField(unique=True)
    url_name = models.SlugField(unique=True)


class Holiday(models.Model):
    name = models.CharField(max_length=255)
    url_name = models.SlugField(unique=True)
    international = models.BooleanField(default=False)
    worldwide = models.BooleanField(default=False)
    ordinary_holiday = models.BooleanField(default=False)