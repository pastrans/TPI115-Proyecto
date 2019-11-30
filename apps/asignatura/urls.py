from django.urls import path
from apps.asignatura.views import resumenAsignatura, agregarAsignatura, editarAsignatura, estadoAsignatura

urlpatterns = [
    path('', resumenAsignatura, name='resumenAsignatura'),
    path('agregar', agregarAsignatura, name='agregarAsignatura'),
    path('editar/<int:idAsignatura>', editarAsignatura, name='editarAsignatura'),
    path('cambiarEstado/<int:idAsignatura>/<slug:estado>', estadoAsignatura, name='estadoAsignatura'),
]