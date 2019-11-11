from django.db import models

# Create your models here.
class Tiempo(models.Model):
    idTiempo = AutoField(primary_key=True)
    horaInicial = TimeField(auto_now=False)
    horaFinal = TimeField(auto_now=False)
    ESTADO = (
        ('A', 'ACTIVA'),
        ('I', 'INACTIVA')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')