from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('about-site/', views.about_site, name='about-site'),
    path('add-holiday/', views.add_holiday, name='add-holiday'),
    path('contacts/', views.contacts, name='contacts'),
    path('feedback/', views.feedback, name='feedback'),
    path('month/<slug:slug_month>/', views.month, name='month'),
    path('month/<slug:slug_month>/day/<slug: slug_day>', views.day, name='day')
]
