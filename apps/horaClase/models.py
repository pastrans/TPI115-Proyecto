from django.db import models
from apps.tiempo.models import Tiempo
from apps.asignatura.models import Asignatura
from apps.seccionGrado.models import SeccionGrado
from apps.personal.models import Personal

# Create your models here.
class HoraClase(models.Model):
    idHoraClase = models.AutoField(primary_key=True)
    asignatura = models.ForeignKey(Asignatura, null=False, blank=False, on_delete=models.CASCADE)
    seccionGrado = models.ForeignKey(SeccionGrado, null=False, blank=False, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, null=False, blank=False, on_delete=models.CASCADE)
    tiempo = models.ForeignKey(Tiempo, null=False, blank=False, on_delete=models.CASCADE)
    DIA = (
        ('L', 'LUNES'),
        ('M', 'MARTES'),
        ('X', 'MIÉRCOLES'),
        ('J', 'JUEVES'),
        ('V', 'VIERNES')
    )
    dia = models.CharField(max_length=1, choices=DIA, default='L')