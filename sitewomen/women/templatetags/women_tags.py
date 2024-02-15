from django import template
import women.views as views
from women.models import Category

register = template.Library()


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.all().order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}