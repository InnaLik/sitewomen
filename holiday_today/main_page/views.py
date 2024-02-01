from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
from .models import Month, Day, Holiday


def main(request):
    return render(request, 'main_page.index.html')


def base(request):
    month = Month.objects.all()
    data = [{'name': 'О сайте', 'url_name': 'about-site'},
            {'name': 'Добавить праздник', 'url_name': 'add-holiday'},
            {'name': 'Контакты', 'url_name': 'contacts'},
            {'name': 'Обратная связь', 'url_name': 'feedback'}]
    d = {'data': data,
         'month': month}
    return render(request, 'base.html', d)


def about_site(request):
    return HttpResponse('О сайте')


def add_holiday(request):
    return HttpResponse('Добавить праздник')


def contacts(request):
    return HttpResponse('Контакты')


def feedback(request):
    return HttpResponse('Обратная связь')

def month(request, slug_month):
    post = get_object_or_404(Month, url_name=slug_month)
    day = Day.objects.all()
    d = {'day': day,
         'month': slug_month}
    return render(request, 'main_page/month.html', d)


def day(request, slug_month, slug_day):
    k = {'November': 11}
    post = get_object_or_404(Day, url_name=slug_day)
    holidays = Holiday.objects.filter(date_day=slug_day, date_month=k[slug_month])
    d = {'holidays': holidays}
    return render(request, 'main_page/holidays.html')

def holiday(request, slug_month, slug_day, slug_holiday):
    pass



