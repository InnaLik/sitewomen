from django.db import models

# Create your models here.
#такая табличка будет в бд
class Women(models.Model): #именно это наследование превращает наш в класс в обхект модели
    title = models.CharField(max_length=255) #текстовые поля
    content = models.TextField(blank=True) #blank позволяет нам не задавать значение поля при записи таблицы
    time_create = models.DateTimeField(auto_now_add=True) #auto автоматически будет заполнять поле, но только в момент первого появления данной записи
    time_update = models.DateTimeField(auto_now=True) #меняется каждый раз при записи в базу данных (автоматически)
    is_published = models.BooleanField(default=True)

