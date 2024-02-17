

from django.db import models

# Create your models here.
from django.urls import reverse


class Month(models.Model):
    number_month = models.IntegerField(unique=True)
    name_month = models.CharField(max_length=255, unique=True)
    count_day = models.IntegerField()
    slug = models.SlugField(db_index=True, unique=True)

    def get_absolute_url(self):
        #  первый аргумент это именно название нашей функции во views
        return reverse('see_month', kwargs={'slug_months': self.slug})

    def __str__(self):
        return self.name_month



class Day(models.Model):
    number_day = models.IntegerField(unique=True)
    url_name = models.SlugField(unique=True)
    is_published = models.BooleanField(default=True)


    # 'month/<slug:slug_month>/<slug:slug_day>/'



class Holiday(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'черновик'
        PUBLISHED = 1, 'опубликовано'
    name = models.CharField(max_length=255)
    url_name = models.SlugField(unique=True)
    international = models.BooleanField(default=False)
    worldwide = models.BooleanField(default=False)
    ordinary_holiday = models.BooleanField(default=False)
    month = models.ForeignKey(Month, on_delete=models.PROTECT)
    day = models.ForeignKey(Day, on_delete=models.PROTECT)


    def get_absolute_url(self):
        return reverse('day', kwargs={'slug_holiday': self.url_name})

    objects = models.Manager()




# number_month = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# name_month = ['Февраль', "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
# count_day = [29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# url_name = ['February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
