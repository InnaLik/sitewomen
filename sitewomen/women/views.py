from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.defaultfilters import slugify

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]
data_db = [{'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_publisher': True},
           {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_publisher': False},
           {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_publisher': True}]


def index(request):
    # если в шаблоне хотим отобразить две переменные - то ,<p>{{первая переменная}} {{вторая переменная}}</p>
    data = {'title': 'главная страница',
            'menu': menu,
            'posts': data_db}
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {'title': 'О сайте',
            'menu': menu}
    return render(request, 'women/about.html', data)


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id= {post_id}')


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
