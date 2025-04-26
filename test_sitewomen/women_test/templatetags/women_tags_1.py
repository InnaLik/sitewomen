from django import template
import women_test.views as views

# для регистрации новых тегов
register = template.Library()

@register.simple_tag(name='getcats')
def get_categories():
    return views.cats_db

#будет возвращать сформированную html страницу
@register.inclusion_tag('women_test/list_categories.html')
def show_categories(cat_selected=0):
    cats = views.cats_db
    return {'cats': cats, 'cat_selected': cat_selected}