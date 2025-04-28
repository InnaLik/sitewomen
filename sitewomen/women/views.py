from django.http import HttpResponse


def index(request):
    """Главная страница сайта."""
    return HttpResponse("Главная страница")