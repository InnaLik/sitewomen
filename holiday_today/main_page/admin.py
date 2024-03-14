from django.contrib import admin

from main_page.models import Month, Day, Holiday

admin.site.register(Month)
admin.site.register(Day)

admin.site.site_header = 'Календарь праздников'
admin.site.index_title = 'Праздники'

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ['name', 'international', 'worldwide', 'ordinary_holiday', 'slug', 'get_country']
    list_display_link = ['name']
    actions = ['set_international']

    @admin.action(description='Сделать международными')
    def set_international(self, request, queryset):
        count = queryset.update(international=True)
        self.message_user(request, f'{count} праздников сделаны международными')

    @admin.display(description='Страна')
    def get_country(self, holiday: Holiday):
        return [i.title for i in holiday.country.all()]

