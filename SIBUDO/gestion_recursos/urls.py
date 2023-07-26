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

from gestion_recursos import views

urlpatterns = [
    path('libros/', views.gestion_libros, name="Gestion libros"),
    path('libros/agregar', views.agregar_libro, name="Agregar libro"),
    path('libros/eliminar/<int:libro_id>/', views.eliminar_libro, name="Eliminar libro"),
    path('libros/editar/<int:libro_id>/', views.editar_libro, name="Editar libro"),
    
    path('trabajos/', views.gestion_trabajos, name="Gestion trabajos"),
    path('trabajos/agregar', views.agregar_trabajo, name="Agregar trabajo"),
    path('trabajos/eliminar/<int:trabajo_id>/', views.eliminar_trabajo, name="Eliminar trabajo"),
    path('trabajos/editar/<int:trabajo_id>/', views.editar_trabajo, name="Editar trabajo"),
]
