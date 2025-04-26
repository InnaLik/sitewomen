from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'holidays/main_page.html')

data = {'january': 31,
        'february': 29,
        'march': 31,
        'april': 30,
        'may': 31,
        'june': 30,
        'july': 31,
        'august': 31,
        'september': 30,
        'october': 31,
        'november': 30,
        'december': 31}

def day(request, month, day):
    if month in data:
        if day <= data[month]:
            return HttpResponse(f'{month} {day} отмечаются следующие праздники')
        else:
            return HttpResponse('Такого дня нет в этом месяце')
    else:
        return HttpResponse('Такого месяца не существует')