from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.defaultfilters import cut


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]
def main_page(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'data_db': data_db
            }
    return render(request, 'women_test/index.html', context=data)


def about(request):
    data = {'title': 'О сайте',
            'menu': menu}
    return render(request, 'women_test/about.html', context=data)

def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>: {cat_id}')


def categories_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>: {cat_slug}')


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('music',))
        return redirect(uri, permanent=True)
    return HttpResponse(f'Архив по годам {year}')


def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')

