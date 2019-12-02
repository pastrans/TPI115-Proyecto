from django.urls import path
from apps.grado.views import *

urlpatterns = [
    path('', resumenGrado, name='resumenGrado'),
    path('agregar', agregarGrado, name='agregarGrado'),
    path('editar/<int:idGrado>', editarGrado, name='editarGrado'),
    path('cambiarEstado/<int:idGrado>/<slug:estado>', estadoGrado, name='estadoGrado'),
]
