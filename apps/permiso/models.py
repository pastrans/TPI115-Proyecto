from django.db import models
from apps.modulo.models import Modulo

# Create your models here.
class Permiso(models.Model):
    idPermiso = AutoField(primary_key=True)
    nombre = CharField(max_length=50)
    ESTADO = (
        ('A', 'ACTIVA'),
        ('I', 'INACTIVO')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')
    modulo = models.ManyToManyField(Modulo)