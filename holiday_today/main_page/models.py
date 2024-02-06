

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
    is_published = models.BooleanField(default=True)

    # 'month/<slug:slug_month>/<slug:slug_day>/'

class Published(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)


class Holiday(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'черновик'
        PUBLISHED = 1, 'опубликовано'
    name = models.CharField(max_length=255)
    url_name = models.SlugField(unique=True)
    international = models.BooleanField(default=False)
    worldwide = models.BooleanField(default=False)
    ordinary_holiday = models.BooleanField(default=False)
    date_month = models.IntegerField(default=1)
    date_day = models.IntegerField(default=1)
    is_published = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)
    cat_id = models.ForeignKey('Category', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('day', kwargs={'slug_holiday': self.url_name})

    published = Published()
    objects = models.Manager()


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

