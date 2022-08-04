from django.urls import path
from Cliente.views import *


urlpatterns = [
    path('inicio/', inicio),
    path('cliente/', data)
]
