from django.shortcuts import render
from django.urls import path
from . import views

app_name ='stockmanager'

urlpatterns = [
    path('', views.home, name='home'),
    path('add-category/', views.add_category, name='add_category'),
    path('delete_category/<int:pk>/', views.delete_category, name="delete_category"),
    path('add-item/', views.add_item, name='add_item'),
    path('items-list/', views.list_item, name='list_item'),
    path('update-item/<int:pk>/', views.update_item, name='update_item'),
    path('item-detail/<int:pk>/', views.item_detail, name="item_detail"),
    path('delete_item/<int:pk>/', views.delete_item, name="delete_item"),
    path('issue-items/<int:pk>/', views.issue_items, name="issue_items"),
    path('receive-items/<int:pk>/', views.receive_items, name="receive_items"),
    path('reorder-level/<int:pk>/', views.reorder_level, name="reorder_level"),
]