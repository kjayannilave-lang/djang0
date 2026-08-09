from django.urls import path
from . import views

urlpatterns = [
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
]