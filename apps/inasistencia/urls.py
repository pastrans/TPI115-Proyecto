from django.urls import path
from apps.inasistencia.views import pasarAsistencia, importCsv

urlpatterns = [
    path('pasar', pasarAsistencia, name='pasarAsistencia'),
    path('csv/<slug:fecha>', importCsv, name='importCsv'),
]