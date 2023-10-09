from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, render

# Create your views here.
from django.urls import reverse

data_db = [{'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины', 'is_publisher': True},
           {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_publisher': False},
           {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_publisher': True}]

menu = [{'title': 'О сайте', 'url_name': 'home'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}]


def start(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db}
    return render(request, 'child/start.html', context=data)

def page(request):
    return render(request, 'child/page.html', {'title': 'О сайте', 'menu': menu})

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')