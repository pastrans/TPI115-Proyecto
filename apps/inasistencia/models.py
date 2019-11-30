from django.db import models
from apps.estudiante.models import Estudiante
from apps.seccionGrado.models import SeccionGrado
import io, os, datetime
os.environ['TZ'] = 'America/El_Salvador'

# Create your models here.
class Inasistencia(models.Model):
    idInasistencia = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.date.today())
    ESTADO = (
        ('J', 'JUSTIFICADA'),
        ('I', 'INJUSTIFICADA')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='I')

class AsistenciaGrado(models.Model):
    idAsistenciaGrado = models.AutoField(primary_key=True)
    fecha = models.DateField(default=datetime.date.today())
    seccionGrado = models.ForeignKey(SeccionGrado, blank=True, on_delete=models.CASCADE)