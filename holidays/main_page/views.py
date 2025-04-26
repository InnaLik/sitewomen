from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

data = [{'id': 1, 'name_holiday': 'Happy New Year', 'url_name': 'new_year', 'description': 'Новый год'},
        {'id': 2, 'name_holiday': 'one september', 'url_name': 'one_september', 'description': '1 сентября'},
        {'id': 3, 'name_holiday': 'saint valentines day', 'url_name': 'valentines_day',
         'description': 'День всех влюбленных'}]

menu = [{'name': 'О сайте', 'url_name': 'about_site'},
        {'name': 'Добавить информацию по празднику', 'url_name': 'add_holiday'},
        {'name': 'Контакты', 'url_name': 'contacts'},
        {'name': 'Обратная связь', 'url_name': 'feedback'}]

# Create your views here.
def start_page(request):
    return render(request, 'main_page/start_page.html', context={'data': data,
                                                                 'menu': menu})


def month_day(request, id_month, id_day):
    return HttpResponse(f'месяц: {id_month} день {id_day}')


def name_holiday(request, holiday_name):
    if holiday_name == 'aaa':
        raise Http404
    return HttpResponse(f'{holiday_name}\n' * 10)


def page_not_found(request, exception):
    return redirect('start_page_app')


def new_year(request):
    return HttpResponse('Новый год')


def one_september(request):
    return HttpResponse('Первое сентября')


def valentines_day(request):
    return HttpResponse('День всех влюбленных')


def about_site(request):
    return HttpResponse('О сайте')


def add_holiday(request):
    return HttpResponse('Добавить статью')


def contacts(request):
    return HttpResponse('Контакты')


def feedback(request):
    return HttpResponse('Обратная связь')