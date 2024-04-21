from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Women, Category

admin.site.site_header = 'Панель администрирования'

admin.site.index_title = 'Известные женщины мира'


class MariedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    # request - объект запроса, этот метод возвращает список из возможных значений параметра статус
    def lookups(self, request, model_admin):
        return [('married', 'Замужем'),
                ('single', 'Не замужем')]

    # queryset - набор записей, из которых мы можем отбирать для фильтра те или иные записи
    def queryset(self, request, queryset):
        # self.value - возвращает значение параметра статус
        if self.value() == 'married':
            return queryset.filter(husb__isnull=False)
        return queryset.filter(husb__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    # поля, которые будут отображаться в форме редактирования
    fields = ['title', 'slug', 'content', 'photo', 'photo_info', 'cat', 'husb', 'tagies']
    # либо можем прописать exclude вместо fields, он исключит поля
    # exclude = ['tagies', 'is_published']
    # поля только для чтения
    readonly_fields = ['photo_info']
    # для автоматического формирования слага
    prepopulated_fields = {'slug': ('title', )}
    # для горизонтального отображения
    # filter_horizontal = ['tagies']
    # для вертикального отображения
    filter_vertical = ['tagies']
    list_display = ('title', 'photo_info', 'time_create', 'is_published', 'cat')
    # кликабельность
    list_display_links = ('title',)
    # порядок сортировки исключительно для отображения в админ панели
    ordering = ['-time_create', 'title']
    # ordering = ['-time_create']
    # поля для редактирования
    list_editable = ['is_published']
    # пагинация списка - максимальное количество статей для отображения на странице
    list_per_page = 20
    # действия
    actions = ['set_published', 'set_draft']
    # указываем список полей, по которым будет осуществляться поиск
    search_fields = ['title__startswith', 'cat__name']
    # панель фильтрации
    list_filter = [MariedFilter, 'cat__name', 'is_published']
    # панель сохранить сверху
    save_on_top = True

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, women: Women):
        return f'Описание {len(women.content)} символов'


    @admin.display(description='photo')
    def photo_info(self, women: Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}' width=50>")


    # для того чтобы действие было делать статьи опубликованными
    # queryset - это коллекция объектов
    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей')

    @admin.action(description='Снять с публикации')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'{count} записей снято с публикации', messages.WARNING)


# admin.site.register(Women, WomenAdmin)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # кликабельность
    list_display_links = ('id', 'name')
