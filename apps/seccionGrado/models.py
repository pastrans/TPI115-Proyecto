from django.db import models
from apps.grado.models import Grado
from apps.seccion.models import Seccion
from apps.especialidad.models import Especialidad
from apps.personal.models import Personal

# Create your models here.
class SeccionGrado(models.Model):
    idSeccionGrado = models.AutoField(primary_key=True)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion, null=False, blank=False on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, null=False, blank=False on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    TURNO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino')
    )
    turno = models.CharField(max_length=1, choices=TURNO, default='M')
    anio = models.IntegerField()