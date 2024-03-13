from django.contrib import admin, messages
from .models import Women, Category

admin.site.site_header = 'Панель администрирования'

admin.site.index_title = 'Известные женщины мира'
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

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, women: Women):
        return f'Описание {len(women.content)} символов'

    # для того чтобы действие было делать статьи опубликованными
    #queryset - это коллекция объектов
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
