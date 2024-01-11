from django.contrib import admin
from django.urls import path, include, re_path, register_converter
from . import views
from . import convertors
# для регистрации конвертора
register_converter(convertors.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.main_page, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),

]
