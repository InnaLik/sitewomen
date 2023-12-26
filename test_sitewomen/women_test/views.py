from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
def main_page(request):
    data = {'title': 'Главная страница',
                     'menu': menu,
            'float': 28.56,
            'lst': [1, 2, 'abs', True],
            'set': {1, 2, 3, 5},
            'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
            'obj': MyClass(10, 20)
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