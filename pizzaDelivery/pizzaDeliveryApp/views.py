from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

from django.shortcuts import render

#funções para renderizar templates
def home(request):
    return render(request, 'pizzaDeliveryApp/home.html')

def cliente(request):
    return render(request, 'pizzaDeliveryApp/cliente.html')

def menu(request):
    return render(request, 'pizzaDeliveryApp/menu.html')