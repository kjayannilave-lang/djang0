from django.urls import path
from . import views

urlpatterns = [
    path('', views.color_form, name='color_form'),
]