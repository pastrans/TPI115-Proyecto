from django.urls import path
from apps.estudiante.views import resumenEstudiante, agregarEstudiante, editarEstudiante, cambiarEstado

urlpatterns = [
    path('', resumenEstudiante, name='resumenEstudiante'),
    path('agregar', agregarEstudiante, name='agregarEstudiante'),
    path('editar/<int:idEstudiante>', editarEstudiante, name='editarEstudiante'),
    path('cambiarEstado/<int:idEstudiante>/<slug:estado>', cambiarEstado, name='cambiarEstado')
]