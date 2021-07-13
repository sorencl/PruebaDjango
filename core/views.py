from core.forms import VehiculoForm
from core.forms import PersonaForm
from django.shortcuts import render, redirect
from .models import Vehichulo
from .models import Persona
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def infoauto(request):
    return render(request, 'core/infoauto.html')


def usuario(request):
    dato1 = {
        'form':PersonaForm()
    }
    if request.method == 'POST':
        formularioPersona = PersonaForm(request.POST)
        if formularioPersona.is_valid:
            formularioPersona.save()
            dato1['mensaje1'] = "Se ha guardado correctamente."
    return render(request, 'core/usuario.html', dato1)


def auto(request):
    datos = {
        'form':VehiculoForm()
    }
    if request.method == 'POST':
        formularioAuto = VehiculoForm(request.POST)
        if formularioAuto.is_valid:
            formularioAuto.save()
            datos['mensaje'] = "Se ha guardado correctamente."
    return render(request, 'core/auto.html',datos)

def autoEdit(request):

    autos = Vehichulo.objects.all()
    dato = {
        'listaAutos':autos
    }

    return render(request, 'core/autoEdit.html',dato)

def usuarioEdit(request):

    usuarios = Persona.objects.all()
    dato2 = {
        'listaPersona':usuarios
    }
    return render(request, 'core/usuarioEdit.html',dato2)

def mod_vehiculo(request,id):
    vehiculo = Vehichulo.objects.get(patente=id)
    datos = {
        'form': VehiculoForm(instance=vehiculo)
    }
    if request.method == 'POST':
        formulario1 = VehiculoForm(data=request.POST, instance=vehiculo)
        if formulario1.is_valid:
            formulario1.save()

            datos['mensaje'] = "Modificado correctamente"
    return render(request, 'core/mod_vehiculo.html',datos)

def mod_persona(request,id):
    persona = Persona.objects.get(rutPersona=id)
    dato3 = {
        'form': PersonaForm(instance=persona)
    }
    return render(request, 'core/mod_persona.html',dato3)


def mod_del_vehiculo(request, id):
    vehiculo = Vehichulo.objects.get(patente = id)
    vehiculo.delete()

    return redirect(to="index")

def mod_del_persona(request, id):
    persona = Persona.objects.get(rutPersona = id)
    persona.delete()

    return redirect(to="index")