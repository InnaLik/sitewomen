from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'main_page.index.html')


def base(request):
    data = [{'name': 'О сайте', 'url_name': 'about-site'},
            {'name': 'Добавить праздник', 'url_name': 'add-holiday'},
            {'name': 'Контакты', 'url_name': 'contacts'},
            {'name': 'Обратная связь', 'url_name': 'feedback'}]
    d = {'data': data}
    return render(request, 'base.html', d)


def about_site(request):
    return HttpResponse('О сайте')


def add_holiday(request):
    return HttpResponse('Добавить праздник')


def contacts(request):
    return HttpResponse('Контакты')


def feedback(request):
    return HttpResponse('Обратная связь')