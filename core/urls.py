from django.urls import path
from .views import index
from .views import infoauto
from .views import trabajos
from .views import formulario
from .views import persona

urlpatterns = [

    path('', index,name="index"),
    path('infoauto/', infoauto,name="infoauto"),
    path('trabajos/', trabajos,name="trabajos"),
    path('formulario/',formulario,name="formulario"),
    path('persona/',persona,name="persona"),

]