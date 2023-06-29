from django.shortcuts import render

# Create your views here.

def gestion_libros(request):
    return render(request, "gestion_recursos/gestion_libros.html")

def gestion_tesis(request):
    return render(request, "gestion_recursos/gestion_tesis.html")