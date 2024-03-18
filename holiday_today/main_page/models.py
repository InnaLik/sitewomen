

from django.db import models

# Create your models here.
from django.urls import reverse


class Month(models.Model):
    number_month = models.IntegerField(unique=True)
    name_month = models.CharField(max_length=255, unique=True)
    count_day = models.IntegerField()
    slug = models.SlugField(db_index=True, unique=True)
    day = models.ManyToManyField('Day', blank=True, related_name='days')

    def get_absolute_url(self):
        #  первый аргумент это именно название нашей функции во views
        return reverse('see_month', kwargs={'slug_months': self.slug})

    def __str__(self):
        return self.name_month

    def get_name_month(self):
        return self.name_month

    class Meta:
        verbose_name_plural = 'Месяцы'


class Day(models.Model):
    number_day = models.IntegerField(unique=True)
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=True)
    month = models.ManyToManyField('Month', blank=True, related_name='month')

    class Meta:
        verbose_name_plural = 'Дни'


class Holiday(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    international = models.BooleanField(default=False, verbose_name='Статус международного')
    worldwide = models.BooleanField(default=False, verbose_name='Статус всемирного')
    ordinary_holiday = models.BooleanField(default=False, verbose_name='Статус обычного')
    month = models.ManyToManyField('Month', blank=True)
    day = models.ManyToManyField('Day', blank=True)
    country = models.ManyToManyField('Country', blank=True)




    class Meta:
        verbose_name_plural = 'Праздники'



class Country(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.CharField(max_length=100)


    def __str__(self):
        return self.title