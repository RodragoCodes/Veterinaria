from django.shortcuts import render
from django.http import HttpResponse
from Cliente.models import cliente

# Create your views here.


def inicio(request):
    return render(request, "Cliente/index.html")

def data(request):
    return HttpResponse("vista de cliente")