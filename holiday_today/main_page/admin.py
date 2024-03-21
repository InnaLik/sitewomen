from django.contrib import admin

from main_page.models import Month, Day, Holiday

admin.site.register(Month)
admin.site.register(Day)

admin.site.site_header = 'Календарь праздников'
admin.site.index_title = 'Праздники'

class MonthFilter(admin.SimpleListFilter):
    title = 'Месяц'
    parameter_name = 'month'

    def lookups(self, request, model_admin):
        return [('Сентябрь', 9),
                ('Октябрь', 10),
                ('Ноябрь', 11),
                ('Декабрь', 12),
                ('Январь', 1),
                ('Февраль', 2)]

    def queryset(self, request, queryset):
        d = {'Сентябрь': 9,
             'Октябрь': 10,
             'Ноябрь': 11,
             'Декабрь': 12,
             'Январь': 1,
             'Февраль': 2}
        s = d.get(self.value())
        return queryset.filter(month__number_month=s)

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ['name', 'international', 'worldwide', 'ordinary_holiday', 'slug', 'get_country']
    list_display_link = ['name', 'slug']
    list_editable = ['international', 'worldwide', 'ordinary_holiday']
    actions = ['set_international']
    # список полей для поиска
    search_fields = ['name']
    list_filter = [MonthFilter, 'international', 'worldwide', 'ordinary_holiday']
    fields = ['name', 'slug', 'international', 'worldwide', 'ordinary_holiday', 'country']
    filter_horizontal = ['country']
    prepopulated_fields = {'slug': ('name',)}


    @admin.action(description='Сделать международными')
    def set_international(self, request, queryset):
        # количество измененных записей
        count = queryset.update(international=True)
        self.message_user(request, f'{count} праздников сделаны международными')

    @admin.display(description='Страна')
    def get_country(self, holiday: Holiday):
        return [i.title for i in holiday.country.all()]




