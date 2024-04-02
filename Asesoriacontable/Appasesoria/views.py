from django.shortcuts import render
from Appasesoria.models import Servicio
from Appasesoria.models import Clientes
from Appasesoria.models import Profesional
from django.http import HttpResponse
from django.template import loader
from Appasesoria.forms import Servicio_formulario
from Appasesoria.forms import Cliente_formulario
from Appasesoria.forms import Profesional_formulario

# Create your views here.

def inicio(request):
    return render( request , "padre.html")


def alta_servicio(request,nombre):
    servicio = Servicio(nombre=nombre, presentacion=4567)
    servicio.save()
    texto = f"Se guardo en la BD el servicio: {servicio.nombre} {servicio.presentacion}"
    return HttpResponse(texto)

def clientes(request):
    return render(request, "clientes.html" )

def profesional(request):
    return render(request, "profesional.html")

def ver_servicios(request):
    servicios = Servicio.objects.all()
    dicc = {"servicios": servicios}
    plantilla = loader.get_template("servicios.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def servicio_formulario(request):
    if request.method == "POST":
        
        mi_formulario = Servicio_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data 
            servicio = Servicio( nombre=datos["nombre"], presentacion=datos["presentacion"])
            servicio.save()
            return render(request, "formulario.html")
    return render(request , "formulario.html")

def cliente_formulario(request):
    if request.method == "POST":
        
        mi_formulario = Cliente_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data 
            cliente = Clientes( nombre=datos["nombre"], cuit=datos["cuit"])
            cliente.save()
            return render(request, "formulario_cliente.html")
    return render(request , "formulario_cliente.html")

def profesional_formulario(request):
    if request.method == "POST":
        
        mi_formulario = Profesional_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data 
            profesional = Profesional( nombre=datos["nombre"], cuit=datos["cuit"])
            profesional.save()
            return render(request, "formulario_profesional.html")
    return render(request , "formulario_profesional.html")

def buscar_servicio(request):
    return render(request, "buscar_servicio.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        servicios = Servicio.objects.filter(nombre_icontains= nombre)
        return render( request ,"resultado_busqueda.html" , {"servicios":servicios})
    else:
        return HttpResponse("Ingrese el nombre del servicio")    

