from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("sumar/", views.sumar),
    path("saludar/nombre=<str:estudiante>", views.saludar),
]

# app1/
# app1/sumar
