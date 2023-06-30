from django.contrib import admin
#se importan los modelos del mismo directorio
from .models import Persona, Rol

# Register your models here.

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Rol)