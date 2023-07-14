from django.shortcuts import render

# Create your views here.
def prestamos(request):
    return render(request, "gestion_prestamos/prestamos.html", {})

def gestion_prestamos(request):
    return render(request, "gestion_prestamos/gestion_prestamos.html", {})

def generar_prestamo(request):
    return render(request, "gestion_prestamos/generar_prestamo.html", {})

def recibir_prestamo(request):
    return render(request, "gestion_prestamos/recibir_prestamo.html", {})

def buscar_prestamo(request):
    return render(request, "gestion_prestamos/buscar_prestamo.html", {})

def gestion_sanciones(request):
    return render(request, "gestion_prestamos/gestion_sanciones.html", {})

def generar_sancion(request):
    return render(request, "gestion_prestamos/generar_sancion.html", {})

def visualizar_sanciones(request):
    return render(request, "gestion_prestamos/visualizar_sanciones.html", {})
