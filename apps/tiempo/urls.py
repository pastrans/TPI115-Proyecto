from django.urls import path
from apps.tiempo.views import resumenTiempo, agregarTiempo, cambiarEstado, editarTiempo

urlpatterns = [
    path('',resumenTiempo,name='resumenTiempo'),
    path('agregar',agregarTiempo,name='agregarTiempo'),
    path('editar/<int:idTiempo>',editarTiempo,name='editarTiempo'),
    path('cambiarEstado/<int:idTiempo>/<slug:estado>',cambiarEstado,name='cambiarEstado')
]