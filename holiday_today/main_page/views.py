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
    month = get_object_or_404(Month, slug=slug_months)
    day = month.day.all()
    d = {'month': month,
         'day': day}
    return render(request, 'main_page/month.html', d)


def see_day(request, slug_month, slug_day):
    day = get_object_or_404(Day, slug_month, slug_day)
    d = {'day': day}
    return render(request, 'main_page/day_holiday.html', d)


def see_holiday(request, slug_months, slug_day, slug_holiday):
    #  вернулась к тому с чего начала, еее
    month = get_object_or_404(Month, slug=slug_months)
    holiday = Holiday.objects.get(slug=slug_holiday, day_id=slug_day, month_id=month.pk)
    d = {'holiday': holiday,
         'month': slug_months,
         'day': slug_day,
         'holiday_slug': slug_holiday}
    return render(request, 'main_page/Holiday.html', d)


def about_site(request):
    return HttpResponse('О сайте')


def add_holiday(request):
    return HttpResponse('Добавить праздник')


def contacts(request):
    return HttpResponse('Контакты')


def feedback(request):
    return HttpResponse('Обратная связь')
