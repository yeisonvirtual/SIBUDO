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
