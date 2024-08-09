"""Modulo para manejar las respuestas de las urls"""

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """Aquí se implementará la lógica para la vista inicial"""

    my_list = ["item1", "item2", "item3"]
    my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
    welcome_text = True  # 👈 replace True with False and check welcome text
    context = {"my_list": my_list, "my_dict": my_dict, "welcome_text": welcome_text}
    return render(request, "index.html", context)


# Utilizando ruta dinámica
def saludar(request, estudiante):
    message = f"Bienvenida {estudiante}"
    data = [1, 2, 3, 4]
    return HttpResponse(message)


def sumar(request, num1, num2):
    """Aquí se implementa la suma mediante rutas dinámicas"""
    return HttpResponse(f"El resultado de la suma es { num1 + num2}")


def restar(request, num1, num2):

    return HttpResponse(f"El resultado de la resta es {num1 - num2}")


def multi(request, num1, num2):
    return HttpResponse(f"El resultado de la multiplicaicón es {num1 * num2}")


def dividir(request, num1, num2):
    return HttpResponse(f"El resultado de la multiplicaicón es {num1 / num2}")
