from django.urls import path
from apps.amonestacion.views import amonestacionIndex, amonestacionBuscar, amonestacionEliminar

urlpatterns = [
    path('', amonestacionIndex, name='amonestacionIndex'),
    path('buscar', amonestacionBuscar, name='amonestacionBuscar'),
    path('eliminar/<int:idAmonestacion>/', amonestacionEliminar, name='amonestacionEliminar')
]
