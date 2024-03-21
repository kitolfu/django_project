from django.contrib import admin
from django.urls import path, include

from library import views


app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'), 
    path('autors/', views.authors_list,name='authors'),
    path('books/<int:book_id>', views.book_detail, name='book_detail')
]
