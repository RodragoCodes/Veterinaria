
from django.urls import path
from Cliente.views import *


urlpatterns = [
    path('inicio/', inicio, name= "inicio"),
    path('cliente/', data, name= "cliente"),
    path('formulario/', formularios, name= "formulario"),
    path ('clientes/crear/', Crear_cliente, name= "clientecrear"),
    path("buscar/", buscar_Cliente),
    path ("resultado/", buscar, name= "buscarcliente"),
    path('procedimientos/', data_procedimientos, name= "procedimientos"),
    path('mascotas/', data_mascotas, name= "mascotas"),
    path ('mascota/crear/', Crear_mascota, name= "mascotacrear"),
    path ('procedimiento/crear/', Crear_procedimiento, name= "procedimientocrear")
]
