from django.db import models

# Create your models here.

class libro(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    edicion = models.IntegerField()
    anio = models.IntegerField()
    isbn = models.CharField(max_length=50)
    disponible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.nombre
    
class trabajo(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=50)
    palabras_clave = models.CharField(max_length=50)
    fecha = models.DateField()
    disponible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'

    def __str__(self):
        return self.titulo
    
class cantidad_libro(models.Model):
    libro = models.OneToOneField(libro, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        verbose_name = 'cantidad libro'

    def __str__(self):
        return self.libro
    
class cantidad_trabajo(models.Model):
    trabajo = models.OneToOneField(trabajo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        verbose_name = 'cantidad trabajo'

    def __str__(self):
        return self.trabajo
