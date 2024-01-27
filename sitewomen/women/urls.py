from django.contrib import admin
from django.urls import path, include, re_path, register_converter
from . import views
from . import convertes

register_converter(convertes.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('category/<int:cat_id>/', views.show_category, name='category')

]

