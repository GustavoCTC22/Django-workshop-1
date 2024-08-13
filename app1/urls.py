from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("about-us/", views.about_us, name="aboutus"),
    path("sumar/<int:num1>+<int:num2>", views.sumar),
    path("resta/<int:num1>-<int:num2>", views.restar),
    path("multi/<int:num1>*<int:num2>", views.multi),
    path("multi/<int:num1>/<int:num2>", views.dividir),
    path("saludar/nombre=<str:estudiante>", views.saludar),
]
