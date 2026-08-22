from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_book, name='add_book'),
    path('books/', views.book_list, name='book_list'),
]