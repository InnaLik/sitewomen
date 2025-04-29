from django.urls import path

from women import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cats/<slug:category_slug>/', views.CategoryView.as_view(), name='categories')
]