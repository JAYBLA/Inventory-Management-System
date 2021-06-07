from django.shortcuts import render
from django.urls import path
from . import views

app_name ='stockmanager'

urlpatterns = [
    path('', views.home, name='home'),
    path('add-item/', views.add_item, name='add_item'),
    path('items-list/', views.list_item, name='list_item'),
]