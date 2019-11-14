from django.db import models

# Create your models here.
class Sancion(models.Model):
    idSancion = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=500)
    ESTADO = (
        ('A', 'ACTIVA'),
        ('I', 'INACTIVO')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')
