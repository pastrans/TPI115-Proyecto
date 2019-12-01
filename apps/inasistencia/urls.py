from django.urls import path
from apps.inasistencia.views import pasarAsistencia, importCsv, administrarAsistencia, asistenciaDiferida, justificarView, justificar

urlpatterns = [
    path('', administrarAsistencia, name='administrarAsistencia'),
    path('pasar/<int:idSeccionGrado>', pasarAsistencia, name='pasarAsistencia'),
    path('diferida/<int:idSeccionGrado>/<slug:fecha>', asistenciaDiferida, name='asistenciaDiferida'),
    path('justificar', justificarView, name="justificarView"),
    path('justificar/<int:idInasistencia>', justificar, name="justificar"),
    path('csv/<slug:fecha>', importCsv, name='importCsv'),
]