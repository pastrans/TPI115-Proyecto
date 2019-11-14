from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from apps.personal.models import Personal
from apps.estudiante.models import Estudiante
from apps.permiso.models import Permiso

# Create your models here.

class UserManager(BaseUserManager):

  def _create_user(self, codigo, password):
    if not codigo:
        raise ValueError('El usuario debe tener un correo electrónico')
    now = timezone.now()
    codigo = self.normalize_email(codigo)
    user = self.model(
        codigo=codigo,
        last_login=now,
        date_joined=now
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, codigo, password, **extra_fields):
    return self._create_user(codigo, password)

class Usuario(AbstractBaseUser):
    codigo = models.CharField(max_length=240, unique=True)
    last_login = models.DateTimeField(null=True, blank=True)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE, blank=True, null=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, blank=True, null=True)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE, blank=True, null=True)
    USERNAME_FIELD = 'codigo'
    EMAIL_FIELD = 'codigo'
    REQUIRED_FIELDS = []
    objects = UserManager()