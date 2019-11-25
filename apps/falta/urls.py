from django.urls import path

from apps.falta.views import *

urlpatterns = [
    path('', resumenFalta, name='resumenFalta'),
    path('agregar', agregarFalta, name='agregarFalta'),
    path('editar/<int:idFalta>', editarFalta, name='editarFalta'),
    path('cambiarEstado/<int:idFalta>/<slug:estado>', estadoFalta, name='estadoFalta'),
]
