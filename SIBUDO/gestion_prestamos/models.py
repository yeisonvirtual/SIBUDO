from django.db import models

# Create your models here.
class Prestamo(models.Model):
    # Atributos de modelo
    id_est = models.PositiveBigIntegerField()
    tipo_recurso = models.IntegerField()
    id_recurso = models.IntegerField()
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    estado_prestamo = models.IntegerField()

    # Atributos de creacion y modificacion
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
    
    def __str__():
        return id

class Disponible_a_Prestamo(models.Model):
    # Atributos de modelo
    id_recurso = models.IntegerField()
    n_disponibles = models.IntegerField()
    tipo_recurso = models.IntegerField()
    tipo_prestamo = models.BooleanField()

    # Atributos de creacion y modificacion
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'Disponible_a_Prestamo'
        verbose_name_plural = 'Disponibles_a_Prestamos'

    def __str__():
        return id