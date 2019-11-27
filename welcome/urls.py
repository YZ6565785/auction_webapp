from django.urls import path
from . import views

from django.shortcuts import render

#list views
from .views import ItemListView

urlpatterns = [
    path('', ItemListView.as_view(), name = 'index'),
]
