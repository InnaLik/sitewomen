from django.urls import path, re_path, register_converter

from .converters import *
from .views import *


register_converter(OneConverters, 'y')

urlpatterns = [
    path('', start, name='home'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('page/', page, name='page')

]
