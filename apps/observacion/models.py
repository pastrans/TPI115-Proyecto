from django.db import models
from apps.estudiante.models import Estudiante
from apps.personal.models import Personal

# Create your models here.
class Observacion(models.Model):
    idObservacion = models.AutoField(primary_key=True)
    observacion = models.CharField(max_length=600)
    fecha = models.DateField(auto_now=False)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, null=False, blank=False, on_delete=models.CASCADE)