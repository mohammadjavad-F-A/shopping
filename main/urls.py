from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('search/', search, name='search'),
    path('about/', about, name='about')
]