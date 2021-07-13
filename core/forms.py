from django import forms
from django.forms import ModelForm
from .models import Vehichulo
from .models import Persona

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehichulo
        fields = ['patente','marca','modelo','cliente','color'
        ]

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['rutPersona', 'nombrePersona','numTelefono']