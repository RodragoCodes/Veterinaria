from django.shortcuts import render
from django.http import HttpResponse
from Cliente.models import cliente, procedimientos, mascotas
from Cliente.forms import ClienteFormulario, MascotaFormulario, ProcedimientoFormulario



# Create your views here.


def inicio(request):
   
    return render(request, "Cliente/index.html")

def data(request):
    clientes= cliente.objects.all()
    context = {"clientes" : clientes}
    return render (request, "Cliente/cliente.html", context)

def data_procedimientos(request):
    procedimiento= procedimientos.objects.all()
    context = {"procedimientos" : procedimiento}
    return render (request, "Cliente/procedimientos.html", context)

def data_mascotas(request):
    mascota= mascotas.objects.all()
    context = {"mascotas" : mascota}
    return render (request, "Cliente/mascotas.html", context)

def formularios(request):
    return render(request, "Cliente/formularios.html")

def Crear_cliente(request):
    if request.method == "GET":
        formulario= ClienteFormulario()
        return render(request, "Cliente/formularios.html", {"formulario" : formulario})
    else:  
        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():
            datos= formulario.cleaned_data
            nombre= datos["nombre"]
            email= datos["email"]
            direccion= datos["direccion"]
            ciudad= datos["ciudad"]
            C= cliente(nombre=nombre, direccion=direccion,ciudad=ciudad, email=email)
            C.save()
            return render(request, "Cliente/index.html")
        else:
            return HttpResponse(f"formulario no valido")

def Crear_mascota(request):
    if request.method == "GET":
        formulario= MascotaFormulario()
        return render(request, "Cliente/formularios.html", {"formulario" : formulario})
    else:  
        formulario = MascotaFormulario(request.POST)

        if formulario.is_valid():
            datos= formulario.cleaned_data
            nombre_mascota= datos["nombre_mascota"]
            tipo= datos["tipo"]
            genero= datos["genero"]
            edad= datos["edad"]
            C= mascotas(nombre_mascota=nombre_mascota,tipo=tipo,genero=genero, edad=edad)
            C.save()
            return render(request, "Cliente/index.html")
        else:
            return HttpResponse(f"formulario no valido")

def Crear_procedimiento(request):
    if request.method == "GET":
        formulario= ProcedimientoFormulario()
        return render(request, "Cliente/formularios.html", {"formulario" : formulario})
    else:  
        formulario = ProcedimientoFormulario(request.POST)

        if formulario.is_valid():
            datos= formulario.cleaned_data
            nombre_proce= datos["procedimiento"]
            costo= datos["costo"]
            C= procedimientos(nombre_proce=nombre_proce, costo=costo)
            C.save()
            return render(request, "Cliente/index.html")
        else:
            return HttpResponse(f"formulario no valido")


def buscar_Cliente(request):
    return render (request, "Cliente/formulario_busqueda.html")

def buscar(request):
    cliente_nombre = request.GET.get("Cliente", None)

    if not cliente_nombre:
        return HttpResponse("No indicaste nombre")
    
    cliente_lista= cliente.objects.filter(nombre__icontains= cliente_nombre)
    return render(request, "Cliente/resultado_busqueda.html", {"Cliente" : cliente_lista})
