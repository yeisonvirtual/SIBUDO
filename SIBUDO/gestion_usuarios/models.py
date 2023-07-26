from django.db import models
from django.contrib.auth.models import User
from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db import models

class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gestion_usuarios'

class persona(models.Model):
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero_choices = (
        ('M', 'Masculino'),
        ('F', 'Femenina'),
        ('O', 'Prefiero no definirlo'),
    )
    genero = models.CharField(max_length=1, choices=genero_choices)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return self.nombre