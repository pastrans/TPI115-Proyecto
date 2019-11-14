from django.db import models
from apps.falta.models import Falta
from apps.estudiante.models import Estudiante
from apps.personal.models import Personal
from apps.sancion.models import Sancion
from apps.horaClase.models import HoraClase

# Create your models here.
class Amonestacion(models.Model):
    idAmonestacion = models.AutoField(primary_key=True)
    falta = models.ForeignKey(Falta, blank=False, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, null=False, blank=False, on_delete=models.CASCADE)
    sancion = models.ForeignKey(Sancion, null=True, blank=True, on_delete=models.CASCADE)
    horario = models.ForeignKey(HoraClase, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False)