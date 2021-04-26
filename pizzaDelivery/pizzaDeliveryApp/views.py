from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

from django.shortcuts import render


# funções para renderizar templates
def home(request):
    return render(request, 'pizzaDeliveryApp/home.html')


def listarProdutos(request):
    produtos = Produto.objects.all()
    produto = {'produtos': produtos}
    return render(request, 'pizzaDeliveryApp/cardapio.html', produto)


def cliente(request):
    return render(request, 'pizzaDeliveryApp/cliente.html')
