from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from SIBUDO_app.views import error_404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SIBUDO_app.urls')),
    path('gestion/', include('gestion_recursos.urls')),#home/index
    path('authentication/', include('authentication.urls')),
    path('gestion_recursos/', include('gestion_recursos.urls')),
    path('gestion_usuarios/', include('gestion_usuarios.urls')),
    path('sanciones_estudiante/', include('sanciones_estudiante.urls')),
    path('prestamos/', include('gestion_prestamos.urls')),
    path('authentication/', include('authentication.urls')),
    path('gestion_recursos/', include('gestion_recursos.urls')),
    path('recursos/', include('recursos.urls')),
    path('graficas/', include('grafica.urls')),
]

handler404 = error_404