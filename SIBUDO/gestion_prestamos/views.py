from django.shortcuts import render

# Create your views here.
def prestamos(request):
    return render(request, "gestion_prestamos/prestamos.html", {})

def gestion_prestamos(request):
    return render(request, "gestion_prestamos/gestion_prestamos.html", {})

def gestion_sanciones(request):
    return render(request, "gestion_prestamos/gestion_sanciones.html", {})
