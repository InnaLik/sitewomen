from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


# именно это наследование превращает наш в класс в обхект модели
class Women(models.Model):
    # класс перечислений, должны быть именно кортежами/ 13 02 2024
    class Status(models.IntegerChoices):
        DRAFT = 0, 'черновик'
        PUBLISHED = 1, 'опубликовано'
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    # текстовые поля
    title = models.CharField(max_length=255)
    # blank позволяет нам не задавать значение поля при записи таблицы
    content = models.TextField(blank=True)
    # auto автоматически будет заполнять поле, но только в момент первого появления данной записи
    time_create = models.DateTimeField(auto_now_add=True)
    # меняется каждый раз при записи в базу данных (автоматически)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)
    # это полноценный объект класса категории, а в бд именно cat_id posts- имя атрибута для обратного связывания
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')
    # не нужно указывать параметр on delete
    tagies = models.ManyToManyField('TagPost', blank=True, related_name='tags')
    husb = models.OneToOneField('Husband', on_delete=models.SET_NULL, null=True, blank=True, related_name='women')
    published = PublishedManager()
    objects = models.Manager()

    # чтобы в оболочке при вызове данных из таблицы красиво показывалось
    def __str__(self):
        return self.title

    # используем этот класс, чтобы делалась всегда сортировка при выводе по данно полю
    class Meta:
        ordering = ['-time_create']
        # используем индекс для более быстрой сортировки
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name
