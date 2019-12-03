from django.urls import path
from django.conf.urls import url
from apps.observacion.views import resumenObservacion, agregarObservacion, buscarObservacion, eliminarObservacion

urlpatterns = [
    path('', resumenObservacion, name="resumenObservacion"),
    path('agregar', agregarObservacion, name='agregarObservacion'),
    path('buscar', buscarObservacion, name='buscarObservacion'),
    path('eliminarObservacion/<int:idObservacion>', eliminarObservacion, name='eliminarObservacion'),
] 