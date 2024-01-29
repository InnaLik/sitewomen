from django.db import models
from django.urls import reverse


class Holiday(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    day = models.DateField()
    international = models.BooleanField(default=False)
    worldwide = models.BooleanField(default=False)
    on_russian = models.BooleanField(default=False)
    other_country = models.BooleanField(default=False)
    fill_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)



class Users(models.Model):
    telegram_id = models.IntegerField()
    name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    fill_date = models.DateTimeField(auto_now_add=True)


# если пользователей хочет чтобы ему пришло уведомление об определенном празднике
# дату, наименование и описание праздника пользователь вводит сам
class OneNotifications(models.Model):
    telegram_id = models.IntegerField()
    name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    date_holiday = models.DateTimeField()
    name_holiday = models.CharField(max_length=100)
    desc_holiday = models.TextField(max_length=600)
    fill_date = models.DateTimeField(auto_now_add=True)


# обратная связь
class Feedback(models.Model):
    id_users = models.IntegerField()
    telegram_id = models.IntegerField(blank=True, null=True)
    desc = models.TextField(max_length=1000)



