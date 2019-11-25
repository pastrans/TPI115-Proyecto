from django.urls import path
from apps.tipoFalta.views import *

urlpatterns = [
    path('', resumenTipoFalta, name='resumenTipoFalta'),
    path('agregar', agregarTipoFalta, name='agregarTipoFalta'),
    path('editar/<int:idTipo>', editarTipoFalta, name='editarTipoFalta'),
    path('cambiarEstado/<int:idTipo>/<slug:estado>', estadoTipoFalta, name='estadoTipoFalta'),
]
