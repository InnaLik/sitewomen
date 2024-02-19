from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('about-site/', views.about_site, name='about-site'),
    path('add-holiday/', views.add_holiday, name='add-holiday'),
    path('contacts/', views.contacts, name='contacts'),
    path('feedback/', views.feedback, name='feedback'),
    path('month/<slug:slug_months>/', views.see_month, name='see_month'),
    path('month/<slug:slug_months>/<slug:slug_day>/', views.see_day, name='see_day'),
    path('month/<slug:slug_months>/<slug:slug_day>/<slug:slug_holiday>/', views.see_holiday, name='see_holiday')
]
