from django.urls import path
from apps.impuntualidad.views import impuntualidadIndex, eliminar, buscar

urlpatterns = [
    path('', impuntualidadIndex, name='indexImpuntualidad'),
    path('buscar', buscar, name='buscarImpuntualidad'),
    path('eliminar/<int:idImpuntualidad>', eliminar, name='eliminarImpuntualidad')
]