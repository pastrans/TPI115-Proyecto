from django.urls import path
from apps.inasistencia.views import pasarAsistencia, importCsv, administrarAsistencia, asistenciaDiferida

urlpatterns = [
    path('', administrarAsistencia, name='administrarAsistencia'),
    path('pasar/<int:idSeccionGrado>', pasarAsistencia, name='pasarAsistencia'),
    path('diferida/<int:idSeccionGrado>/<slug:fecha>', asistenciaDiferida, name='asistenciaDiferida'),
    path('csv/<slug:fecha>', importCsv, name='importCsv'),
]