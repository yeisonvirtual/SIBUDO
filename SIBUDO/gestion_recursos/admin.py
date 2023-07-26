from django.contrib import admin
#se importan los modelos del mismo directorio
from .models import libro, trabajo, cantidad_libro, cantidad_trabajo

# Register your models here.

class libro_admin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class trabajo_admin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(libro, libro_admin)
admin.site.register(trabajo, trabajo_admin)
admin.site.register(cantidad_libro)
admin.site.register(cantidad_trabajo)