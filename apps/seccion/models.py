from django.db import models

# Create your models here.
class Seccion(models.Model):
    idSeccion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=5)
    ESTADO = (
        ('A', 'ACTIVA'),
        ('I', 'INACTIVA')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')