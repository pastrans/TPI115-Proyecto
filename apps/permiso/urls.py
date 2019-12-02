from django.urls import path
from django.conf.urls import url
from apps.permiso.views import resumenPermiso, agregarPermiso, cambiarEstado, eliminarPermiso, editarPermiso

urlpatterns = [
    path('', resumenPermiso, name="resumenPermiso"),#Utilizando
    path('agregar', agregarPermiso, name='agregarPermiso'),#Utilizando
    path('cambiarEstado/<int:idPermiso>/<slug:estado>', cambiarEstado, name='cambiarEstado'),#Utilizando
    path('<int:idPermiso>', editarPermiso, name="editarPermiso"),
    path('eliminar/<int:idPermiso>', eliminarPermiso, name="eliminarPermiso"),
]