from django.db import models

# Create your models here.
class Especialidad(models.Model):
    idEspecialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ESTADO = (
        ('A', 'ACTIVO'),
        ('B', 'INACTIVO')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')