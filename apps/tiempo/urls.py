from django.urls import path
from apps.tiempo.views import resumenTiempo, agregarTiempo, cambiarEstado

urlpatterns = [
    path('',resumenTiempo,name='resumenTiempo'),
    path('agregar',agregarTiempo,name='agregarTiempo'),
    path('editar/<int:idTiempo>',agregarTiempo,name='agregarTiempo'),
    path('cambiarEstado/<int:idTiempo>/<slug:estado>',cambiarEstado,name='cambiarEstado')
]