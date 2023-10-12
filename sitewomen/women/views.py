from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.defaultfilters import slugify
menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']
data_db = [{'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_publisher': True},
           {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_publisher': False},
           {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_publisher': True}]
def index(request):
    #если в шаблоне хотим отобразить две переменные - то ,<p>{{первая переменная}} {{вторая переменная}}</p>
    data = {'title': 'главная страница',
            'menu': menu,
            'posts': data_db}
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


