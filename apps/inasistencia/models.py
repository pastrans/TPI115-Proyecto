from django.db import models
from apps.estudiante.models import Estudiante

# Create your models here.
class Inasistencia(models.Model):
    idInasistencia = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)
    ESTADO = (
        ('J', 'JUSTIFICADA'),
        ('I', 'INJUSTIFICADA')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='I')