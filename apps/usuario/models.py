from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from apps.personal.models import Personal
from apps.estudiante.models import Estudiante

# Create your models here.

class UserManager(BaseUserManager):

  def _create_user(self, email, password):
    if not email:
        raise ValueError('El usuario debe tener un correo electrónico')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        last_login=now,
        date_joined=now
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password)

class Usuario(AbstractBaseUser):
    codigo = models.CharField(max_length=240, unique=True)
    last_login = models.DateTimeField(null=True, blank=True)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE, blank=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, blank=True)
    USERNAME_FIELD = 'codigo'
    EMAIL_FIELD = 'codigo'
    REQUIRED_FIELDS = []
    objects = UserManager()