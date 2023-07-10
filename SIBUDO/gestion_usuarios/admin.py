from django.contrib import admin
#se importan los modelos del mismo directorio
from .models import persona, rol

# Register your models here.

class persona_admin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(persona, persona_admin)
admin.site.register(rol)