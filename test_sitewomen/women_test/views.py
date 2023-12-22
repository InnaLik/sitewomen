from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render



def main_page(request):
    return HttpResponse('Это главная страница')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>: {cat_id}')


def categories_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>: {cat_slug}')


def archive(request, year):
    if year > 2023:
        raise Http404()
    return HttpResponse(f'{year}')


def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')