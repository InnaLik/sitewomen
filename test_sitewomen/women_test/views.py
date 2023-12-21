from django.http import HttpRequest, HttpResponse
from django.shortcuts import render



def main_page(request):
    return HttpResponse('Это главная страница')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>: {cat_id}')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>: {cat_slug}')


def archive(request, year):
    return HttpResponse(f'{year}')