from django.db import models

# Create your models here.
class Modulo(models.Model):
    idModulo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)