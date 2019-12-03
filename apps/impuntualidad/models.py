from django.db import models
from apps.estudiante.models import Estudiante
import datetime

# Create your models here.
class Impuntualidad(models.Model):
    idImpuntualidad = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False)
    hora = models.TimeField(default=datetime.datetime.now())
    ESTADO = (
        ('J', 'JUSTIFICADA'),
        ('I', 'INJUSTIFICADA')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='I')