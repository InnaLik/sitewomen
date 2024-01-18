from django.urls import path

from main_page import views

urlpatterns = [
    path('', views.start_page, name='start_page_app'),
    path('month/<int:id_month>/day/<int:id_day>/', views.month_day, name='month_day_app'),
    path('holiday/<str:holiday_name>/', views.name_holiday, name='name_holiday'),
    path('new_year/', views.new_year, name='new_year'),
    path('one_september/', views.one_september, name='one_september'),
    path('valentines_day/', views.valentines_day, name='valentines_day'),
    path('about_site/', views.about_site, name='about_site'),
    path('add_holiday/', views.add_holiday, name='add_holiday'),
    path('contacts/', views.contacts, name='contacts'),
    path('feedback', views.feedback, name='feedback')
]
