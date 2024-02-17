from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
from .models import Month, Day, Holiday

data = [{'name': 'О сайте', 'url_name': 'about-site'},
        {'name': 'Добавить праздник', 'url_name': 'add-holiday'},
        {'name': 'Контакты', 'url_name': 'contacts'},
        {'name': 'Обратная связь', 'url_name': 'feedback'}]
def main(request):
    return render(request, 'main_page.index.html')


def base(request):
    d = {'data': data}
    return render(request, 'base.html', d)




def see_month(request, slug_months):
    month = Month.objects.all().filter(slug=slug_months)
    d = {'month': month,
         'count_day': 31}
    return render(request, 'main_page/month.html', d)


def about_site(request):
    return HttpResponse('О сайте')


def add_holiday(request):
    return HttpResponse('Добавить праздник')


def contacts(request):
    return HttpResponse('Контакты')


def feedback(request):
    return HttpResponse('Обратная связь')

