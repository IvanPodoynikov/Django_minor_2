from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry_list, name='entry_list'),
    path('new/', views.entry_create, name='entry_create'),
    path('stats/', views.entry_stats, name='entry_stats'),
    path('about/', views.about_me, name='about_me')
]