from django.urls import path
from apps.seccionGrado.views import *

urlpatterns = [
    path('', resumenSeccionGrado, name='resumenSeccionGrado'),
    path('agregar', agregarSeccionGrado, name='agregarSeccionGrado'),
    path('editar/<int:idSeccionGrado>', editarSeccionGrado, name='editarSeccionGrado'),
]
