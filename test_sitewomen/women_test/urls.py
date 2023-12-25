from django.contrib import admin
from django.urls import path, include, re_path, register_converter
from . import views
from . import convertors
# для регистрации конвертора
register_converter(convertors.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.main_page, name='home'),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    # path(r'^archive/(?P<year>[0-9]{4})/', views.archive)
    # вместо этого используем конвертер
    path("archive/<year4:year>/", views.archive, name='archive')
]
