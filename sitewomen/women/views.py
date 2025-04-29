from django.http import HttpResponse, HttpResponseNotFound
from django.views import View


class IndexView(View):
    """Главная страница сайта."""
    def get(self, request, *args, **kwargs):
        return HttpResponse("Главная страница")

class CategoryView(View):
    def get(self, request, category_slug):
        return HttpResponse(f"{category_slug}")

class PageNotFoundView(View):
    """Для обработки страницы 404."""
    def get(self, request, *args, **kwargs):
        return HttpResponseNotFound("Страница не существует, не найдена или удалена :(")