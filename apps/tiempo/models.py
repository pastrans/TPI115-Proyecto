from django.db import models

# Create your models here.
class Tiempo(models.Model):
    idTiempo = models.AutoField(primary_key=True)
    horaInicial = models.TimeField(auto_now=False)
    horaFinal = models.TimeField(auto_now=False)
    ESTADO = (
        ('A', 'ACTIVA'),
        ('I', 'INACTIVA')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')