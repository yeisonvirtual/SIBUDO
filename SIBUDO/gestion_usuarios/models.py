from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class rol(models.Model):
    tipo = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.tipo

class persona(models.Model):
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rol = models.OneToOneField(rol, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return self.nombre