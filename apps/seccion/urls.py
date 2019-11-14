from django.urls import path
from apps.seccion.views import resumenSeccion, agregarSeccion, editarSeccion, eliminarSeccion

urlpatterns = [
    path('', resumenSeccion, name='resumenSeccion'),
    path('agregar', agregarSeccion, name='agregarSeccion'),
    path('editar/<int:idSeccion>', editarSeccion, name='editarSeccion'),
    path('eliminar/<int:idSeccion>', eliminarSeccion, name='eliminarSeccion'),
]
