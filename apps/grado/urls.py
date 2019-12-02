from django.urls import path
from apps.grado.views import *

urlpatterns = [
    path('', resumenGrado, name='resumenGrado'),
    path('agregar', agregarGrado, name='agregarGrado'),

]
