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
from .views import mod_vehiculo
from .views import mod_persona
from .views import mod_del_vehiculo
from .views import mod_del_persona

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
    path('mod-vehiculo/<id>',mod_vehiculo,name="mod_vehiculo"),
    path('mod-persona/<id>',mod_persona,name="mod_persona"),
    path('mod-del-vehiculo/<id>',mod_del_vehiculo,name="mod_del_vehiculo"),
    path('mod-del-persona/<id>',mod_del_persona,name="mod_del_persona"),
    
]



