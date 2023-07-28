from django.contrib import admin
from django.urls import path

from grafica import views

urlpatterns = [
    path('charts', views.grafica, name="grafica"),
]
