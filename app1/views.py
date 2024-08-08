from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Este es el index de la aplicación")


# Utilizando ruta dinámica
def saludar(request, estudiante):
    message = f"Bienvenida {estudiante}"
    return HttpResponse(message)


def sumar(request):
    return HttpResponse(f"5 + 10 es igual = {5+10}")


def restar(request):
    pass


def multi(request):
    pass


def dividir(request):
    pass
