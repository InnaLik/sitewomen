from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddFormsHoliday, AddFileUpload
from .models import Month, Day, Holiday, UploadFileModel

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


def see_day(request, slug_months, slug_day):
    month = Month.objects.values('id').get(slug=slug_months)
    holidays = Holiday.objects.filter(month=month['id'], day=slug_day)
    d = {'holidays': holidays,
         'month': slug_months,
         'day': slug_day}
    return render(request, 'main_page/day_holiday.html', d)


def see_holiday(request, slug_months, slug_day, slug_holiday):
    month = get_object_or_404(Month, slug=slug_months)
    holiday = Holiday.objects.get(slug=slug_holiday, day=slug_day, month=month.id)
    d = {'holiday': holiday,
         'month': slug_months,
         'day': slug_day,
         'holiday_slug': slug_holiday}
    return render(request, 'main_page/Holiday.html', d)


# def handle_uploaded_file(f):
#     with open(f"uploads/{f}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

def about_site(request):
    pass


def add_holiday(request):
    if request.method == 'POST':
        form = AddFormsHoliday(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            month = form.cleaned_data['month']
            day = form.cleaned_data['day']
            country = form.cleaned_data['country']
            form.save()
            name = form.cleaned_data['name']
            s = Holiday.objects.get(name=name)
            s.month.add(month)
            s.day.add(day)
            s.country.add(country)
            return redirect('base')

    else:
        form = AddFormsHoliday()
    d = {'form': form}
    return render(request, 'main_page/add_holiday.html', d)


def contacts(request):
    return HttpResponse('Контакты')


def feedback(request):
    return HttpResponse('Обратная связь')
