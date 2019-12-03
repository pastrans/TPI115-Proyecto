from django.urls import path
from django.conf.urls import url
from apps.permiso.views import resumenPermiso, agregarPermiso, cambiarEstado, editarPermiso

urlpatterns = [
    path('', resumenPermiso, name="resumenPermiso"),
    path('agregar', agregarPermiso, name='agregarPermiso'),
    path('cambiarEstado/<int:idPermiso>/<slug:estado>', cambiarEstado, name='cambiarEstado'),
    path('editarPermiso/<int:idPermiso>', editarPermiso, name="editarPermiso"),
]