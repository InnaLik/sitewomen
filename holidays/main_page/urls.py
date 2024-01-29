from django.urls import path

from main_page import views

urlpatterns = [
    path('', views.start_page, name='start_page_app'),
    path('month/<int:id_month>/day/<int:id_day>/', views.month_day, name='month_day_app'),
    path('about_site/', views.about_site, name='about_site'),
    path('add_holiday/', views.add_holiday, name='add_holiday'),
    path('contacts/', views.contacts, name='contacts'),
    path('feedback', views.feedback, name='feedback'),
    path('holiday/<slug:slug_holi>/', views.about_holiday, name='holiday')

]
