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
#     month = Month.objects.all().filter(slug=slug_months)
#     count_day = [i for i in range(1, 32)]
#     return {'month': month, 'count_day': count_day}