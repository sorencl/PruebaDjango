from django.db import models

# Create your models here.

class  Persona(models.Model):
    rutPersona = models.IntegerField(primary_key=True,verbose_name="Rut persona")
    nombrePersona = models.CharField(max_length=50, verbose_name="Nombre de la Persona")
    numTelefono = models.CharField(max_length=12, verbose_name="Numero de telefono")

    def __str__(self):
        return self.nombrePersona

class Vehichulo(models.Model):
    patente = models.CharField(max_length=6,primary_key=True, verbose_name="Patente")
    marca = models.CharField(max_length=20, verbose_name="Marca")
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name="Modelo")
    cliente = models.ForeignKey(Persona, on_delete=models.CASCADE)
    color = models.CharField(max_length=15,verbose_name="Color")

    def __str__(self):
        return self.patente
