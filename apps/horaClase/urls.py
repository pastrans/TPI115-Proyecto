from django.urls import path
from apps.horaClase.views import redirectVacio, resHorarioPnal, resHorarioSecc, agregarHoraClase, eliminarHoraClase

urlpatterns = [
    path('', redirectVacio, name='redirectVacio'),
    path('horarioPersonal/<int:idPnal>', resHorarioPnal, name='resHorarioPnal'),
    path('horarioSeccion/<int:idSecc>', resHorarioSecc, name='resHorarioSecc'),
    path('horarioPersonal/agregar', agregarHoraClase, name='agregarHoraClaseP'),
    path('horarioSeccion/agregar', agregarHoraClase, name='agregarHoraClaseS'),
    path('horarioPersonal/<slug:strOrigen>/eliminar/<int:idHC>', eliminarHoraClase, name='eliminarHoraClaseP'),
    path('horarioSeccion/<slug:strOrigen>/eliminar/<int:idHC>', eliminarHoraClase, name='eliminarHoraClaseS')
]