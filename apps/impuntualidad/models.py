from django.db import models
from apps.estudiante.models import Estudiante

# Create your models here.
class Impuntualidad(models.Model):
    idImpuntualidad = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, blank=False, on_delte=models.CASCADE)
    fechaHora = models.DateField(auto_now=True)
    ESTADO = (
        ('J', 'JUSTIFICADA'),
        ('I', 'INJUSTIFICADA')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='I')