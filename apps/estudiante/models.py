from django.db import models
from apps.seccionGrado.models import SeccionGrado

# Create your models here.
class Estudiante(models.Model):
    idEstudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    ESTADO = (
        ('A', 'ACTIVA'),
        ('I', 'INACTIVO')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')
    seccionGrado = models.ForeignKey(SeccionGrado, on_delete=models.CASCADE, null=True)