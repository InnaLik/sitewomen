from django import template

from main_page.models import Month, Day

register = template.Library()

@register.simple_tag()
def show_month():
    month = Month.objects.all()
    return month

