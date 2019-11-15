from django.urls import path
from apps.seccion.views import resumenSeccion, agregarSeccion, editarSeccion, estadoSeccion

urlpatterns = [
    path('', resumenSeccion, name='resumenSeccion'),
    path('agregar', agregarSeccion, name='agregarSeccion'),
    path('editar/<int:idSeccion>', editarSeccion, name='editarSeccion'),
    path('cambiarEstado/<int:idSeccion>/<slug:estado>', estadoSeccion, name='estadoSeccion'),
]
