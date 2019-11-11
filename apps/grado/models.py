from django.db import models

# Create your models here.
class Grado(models.Model):
    idGrado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    NIVEL = (
        ('T', 'Tercer Ciclo'),
        ('B', 'Bachillerato')
    )
    ESTADO = (
        ('A', 'ACTIVO'),
        ('B', 'INACTIVO')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')
    nivel = models.CharField(max_length=1, choices=NIVEL, default='T')