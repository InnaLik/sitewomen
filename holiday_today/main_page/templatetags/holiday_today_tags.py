from django import template

from main_page.models import Month, Day

register = template.Library()

@register.simple_tag()
def show_month():
    month = Month.objects.all()
    return month


@register.inclusion_tag('women/month.html')
def show_all_tags():
    tags = Day.objects.filter('month_id')
    tags = TagPost.objects.annotate(total=Count("tags")).filter(total__gt=0)
    return {'tags': tags}
