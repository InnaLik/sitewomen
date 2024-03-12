from django.contrib import admin
from .models import Women, Category

admin.site.site_header = 'Панель администрирования'

admin.site.index_title = 'Известные женщины мира'
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'cat')
    # кликабельность
    list_display_links = ('id', 'title')
    # порядок сортировки исключительно для отображения в админ панели
    ordering = ['time_create', 'title']
    # поля для редактирования
    list_editable = ['is_published']
    # пагинация списка - максимальноке количество статей для отображения на странице
    list_per_page = 20



# admin.site.register(Women, WomenAdmin)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # кликабельность
    list_display_links = ('id', 'name')
