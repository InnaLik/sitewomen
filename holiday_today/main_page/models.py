

from django.db import models

# Create your models here.
from django.urls import reverse


class Month(models.Model):
    number_month = models.IntegerField(unique=True)
    name_month = models.CharField(max_length=255, unique=True)
    count_day = models.IntegerField()
    slug = models.SlugField(db_index=True, unique=True)
    day = models.ManyToManyField('Day', blank=True)


    def get_absolute_url(self):
        #  первый аргумент это именно название нашей функции во views
        return reverse('see_month', kwargs={'slug_months': self.slug})

    def __str__(self):
        return self.name_month


class Day(models.Model):
    number_day = models.IntegerField(unique=True)
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=True)

    # 'month/<slug:slug_month>/<slug:slug_day>/'
    def get_absolute_url(self):
        #  первый аргумент это именно название нашей функции во views
        return reverse('see_day', kwargs={'slug_day': self.slug})

class Holiday(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    international = models.BooleanField(default=False)
    worldwide = models.BooleanField(default=False)
    ordinary_holiday = models.BooleanField(default=False)
    month = models.ForeignKey(Month, on_delete=models.PROTECT)
    day = models.ForeignKey(Day, on_delete=models.PROTECT)







    # number_month = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# name_month = ['Февраль', "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
# "Ноябрь", "Декабрь"]
# count_day = [29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# url_name = ['February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
# 'November', 'December']
