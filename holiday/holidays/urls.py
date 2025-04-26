from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('<str:month>/<int:day>/', views.day, name='day')
]
