from django import template

from main_page.models import Month, Day

register = template.Library()

@register.simple_tag()
def show_month():
    month = Month.objects.all()
    return month

# @register.simple_tag()
# def show_day():
#     month = Day.objects.all()
#     return month


# @register.inclusion_tag('main_page/month.html')
# def show_day(slug_months):
#     month = Month.objects.all().filter
#     day = Day.objects.all()
#     return {'month': month, 'day': day}