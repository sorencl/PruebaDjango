from core.forms import VehiculoForm
from django.shortcuts import render
from .models import Vehichulo, Persona
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def infoauto(request):
    return render(request, 'core/infoauto.html')

def trabajos(request):
    return render(request, 'core/trabajos.html')

def formulario(request):
    datos = {
        'form':VehiculoForm()
    }
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"

    
    return render(request, 'core/formulario.html', datos)

def persona(request):
    datos = {
        'form': PersonaForm()
        
    }

    return render(request, 'core/persona.html')


def usuario(request):
    return render(request, 'core/usuario.html')


def auto(request):
    return render(request, 'core/auto.html')

def autoEdit(request):
    return render(request, 'core/autoEdit.html')

def usuarioEdit(request):
    return render(request, 'core/usuarioEdit.html')