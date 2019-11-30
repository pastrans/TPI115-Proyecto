from django.urls import path
from apps.horaClase.views import redirectVacio, resHorarioPnal, resHorarioSecc

urlpatterns = [
    path('', redirectVacio, name='redirectVacio'),
    path('horarioPersonal/<int:idPnal>', resHorarioPnal, name='resHorarioPnal'),
    path('horarioSeccion/<int:idSecc>', resHorarioSecc, name='resHorarioSecc'),
]