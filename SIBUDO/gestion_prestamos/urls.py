"""
URL configuration for proyecto_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from gestion_prestamos import views

urlpatterns = [
    path('', views.prestamos, name="Prestamos"),
    path('gestion_prestamos/', views.gestion_prestamos, name="Gestion_Prestamos"),
    path('generar_prestamo/', views.generar_prestamo, name="Generar_Prestamo"),
    path('guardar_prestamo/', views.guardar_prestamo, name="Guardar_Prestamo"),
    path('guardar_prestamo/<int:id_est>/<int:tipo_rec>/<int:id_rec>/', views.guardar_prestamo, name="Guardar_Prestamo"),
    path('recibir_prestamo/', views.recibir_prestamo, name="Recibir_Prestamo"),
    path('recibir_prestamo/<int:id_prestamo>/', views.recibir_prestamo, name="Recibir_Prestamo"),
    path('mensaje_resultado/<int:id_prestamo>/', views.mensaje_resultado, name="Mensaje_Resultado"),
    path('editar_prestamo/<int:id_prestamo>/', views.editar_prestamo, name="Editar_Prestamo"),
    path('buscar_prestamo/', views.buscar_prestamo, name="Buscar_Prestamo"),
    path('gestion_sanciones/', views.gestion_sanciones, name="Gestion_Sanciones"),
    path('generar_sancion/', views.generar_sancion, name="Generar_Sancion"),
    path('sancionar/<int:id_prestamo>/', views.sancionar, name="Sancionar"),
    path('visualizar_sanciones/', views.visualizar_sanciones, name="Visualizar_Sanciones"),
]