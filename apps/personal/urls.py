from django.urls import path
from apps.personal.views import resumenPersonal, agregarPersonal, editarPersonal, cambiarEstado

urlpatterns = [
    path('', resumenPersonal, name='resumenPersonal'),
    path('agregar', agregarPersonal, name='agregarPersonal'),
    path('editar/<int:idPnal>', editarPersonal, name='editarPersonal'),
    path('cambiarEstado/<int:idPnal>/<slug:estado>', cambiarEstado, name='cambiarEstado')
]