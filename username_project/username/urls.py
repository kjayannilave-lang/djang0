from django.urls import path
from . import views

urlpatterns = [
    path('', views.username_form, name='username_form'),
    path('result/', views.result, name='result'),
]