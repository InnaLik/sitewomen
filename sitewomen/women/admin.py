from django.contrib import admin, messages
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
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    # кликабельность
    list_display_links = ('title',)
    # порядок сортировки исключительно для отображения в админ панели
    ordering = ['-time_create', 'title']
    # ordering = ['-time_create']
    # поля для редактирования
    list_editable = ['is_published']
    # пагинация списка - максимальное количество статей для отображения на странице
    list_per_page = 20
    actions = ['set_published', 'set_draft']
    # указываем список полей, по которым будет осуществляться поиск
    search_fields = ['title__startswith', 'cat__name']
    # панель фильтрации
    list_filter = [MariedFilter, 'cat__name', 'is_published']

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, women: Women):
        return f'Описание {len(women.content)} символов'

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
