from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse


def main_page(request):
    return render(request, 'women_test/index.html')


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