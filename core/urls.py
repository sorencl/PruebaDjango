from django.urls import path
from .views import index
from .views import infoauto
from .views import trabajos
from .views import formulario
from .views import persona
from .views import auto
from .views import usuario
from .views import autoEdit
from .views import usuarioEdit

urlpatterns = [

    path('', index,name="index"),
    path('infoauto/', infoauto,name="infoauto"),
    path('trabajos/', trabajos,name="trabajos"),
    path('formulario/',formulario,name="formulario"),
    path('persona/',persona,name="persona"),
    path('auto/',auto,name="auto"),
    path('usuario/',usuario,name="usuario"),
    path('usuarioEdit/',usuarioEdit, name="usuarioEdit"),
    path('autoEdit/', autoEdit, name="autoEdit"),

]