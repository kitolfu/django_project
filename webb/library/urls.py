from django.contrib import admin
from django.urls import path, include

from library import views
urlpatterns = [
    path('', views.index),
    path('book/', views.books),
    path('book/<pk>/', views.book)
]
