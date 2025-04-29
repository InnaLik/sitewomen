from django.http import HttpResponse


def index(request):
    """Главная страница сайта."""
    return HttpResponse("Главная страница")

def categories(request, category_slug:str):
    return HttpResponse(f"{category_slug}")