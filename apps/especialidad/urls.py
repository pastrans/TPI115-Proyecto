from django.urls import path
from apps.especialidad.views import resumenEspecialidad, editarEspecialidad, estadoEspecialidad

urlpatterns = [
    path('agregar', resumenEspecialidad, name='agregarEspecialidad'),
    path('editar/<int:idEspecialidad>', editarEspecialidad, name='editarEspecialidad'),
    path('cambiarEstado/<int:idEspecialidad>/<slug:estado>', estadoEspecialidad, name='estadoEspecialidad'),

]