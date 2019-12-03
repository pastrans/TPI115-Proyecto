from django.urls import path
from django.conf.urls import url
from apps.observacion.views import resumenObservacion, agregarObservacion

urlpatterns = [
    path('', resumenObservacion, name="resumenObservacion"),
    path('agregar', agregarObservacion, name='agregarObservacion'),

    #path('cambiarEstado/<int:idPermiso>/<slug:estado>', cambiarEstado, name='cambiarEstado'),#Utilizando
    #path('editarPermiso/<int:idPermiso>', editarPermiso, name="editarPermiso"),#Utilizando
] 