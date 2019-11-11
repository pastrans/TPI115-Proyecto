from django.db import models
from apps.tipoFalta.models import TipoFalta

# Create your models here.
class Falta(models.Model):
    idFalta = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    tipoFalta = models.ForeignKey(TipoFalta, null=False, blank=False, on_delete=models.CASCADE)
    ESTADO = (
        ('A', 'ACTIVA'),
        ('I', 'INACTIVA')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')