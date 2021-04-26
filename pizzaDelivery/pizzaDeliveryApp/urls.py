from django.urls import path
from . import views

# Trigger das funções da views
urlpatterns = [
    path('', views.home),
    path('cliente/', views.cliente),
    path('cardapio/', views.listarProdutos)


]
