from django.db import models

# Create your models here.
#такая табличка будет в бд
from django.urls import reverse


class Women(models.Model): #именно это наследование превращает наш в класс в обхект модели
    title = models.CharField(max_length=255) #текстовые поля
<<<<<<< HEAD
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
=======
    slug = models.SlugField(max_length=255, blank=True, db_index=True, default='')
>>>>>>> 34c923ab9f1d774ab4538e3c993e2eb01c75c4c5
    content = models.TextField(blank=True) #blank позволяет нам не задавать значение поля при записи таблицы
    time_create = models.DateTimeField(auto_now_add=True) #auto автоматически будет заполнять поле, но только в момент первого появления данной записи
    time_update = models.DateTimeField(auto_now=True) #меняется каждый раз при записи в базу данных (автоматически)
    is_published = models.BooleanField(default=True)

    #чтобы в оболочке при вызове данных из таблицы красиво показывалось
    def __str__(self):
        return self.title

    #используем этот класс, чтобы делалась всегда сортировка при выводе по данно полю
    class Meta:
        ordering = ['-time_create']
        #используем индекс для более быстрой сортировки
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})