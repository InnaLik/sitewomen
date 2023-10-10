from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
def index(request):
    #если в шаблоне хотим отобразить две переменные - то ,<p>{{первая переменная}} {{вторая переменная}}</p>
    data = {'title': 'Главная страница',
            'menu': menu,
            'float': 28.56,
            'lst': [1, True],
            'set': {1, 2, 3},
            'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
            'obj': MyClass(10, 20)}
    return render(request, 'women/index.html', context=data)

def about(request):
    data = {'title': 'О сайте'}
    return render(request, 'women/about.html', data)

def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')

def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=['music'])
        return HttpResponseRedirect('home')
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


