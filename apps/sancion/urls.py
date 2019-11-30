from django.urls import path
from apps.sancion.views import resumenSancion, agregarSancion, editarSancion, estadoSancion

urlpatterns = [
    path('', resumenSancion, name='resumenSancion'),
    path('agregar', agregarSancion, name='agregarSancion'),
    path('editar/<int:idSancion>', editarSancion, name='editarSancion'),
    path('cambiarEstado/<int:idSancion>/<slug:estado>', estadoSancion, name='estadoSancion'),
]