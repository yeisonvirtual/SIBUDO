from django.shortcuts import render
from .models import Prestamo
from gestion_usuarios.models import persona
from django.db.models import Q

# Create your views here.
def prestamos(request):
    return render(request, "gestion_prestamos/prestamos.html", {})

def gestion_prestamos(request):
    return render(request, "gestion_prestamos/gestion_prestamos.html", {})

def generar_prestamo(request):
    return render(request, "gestion_prestamos/generar_prestamo.html", {})

def guardar_prestamo(request):
    return render(request, "gestion_prestamos/guardar_prestamo.html", {})

def recibir_prestamo(request):
    return render(request, "gestion_prestamos/recibir_prestamo.html", {})

def buscar_prestamo(request):
    prestamos_a_nd = Prestamo.objects.filter(Q(estado_prestamo=1) | Q(estado_prestamo=2) | Q(estado_prestamo=3))
    list_estud = [None]
    for prestamo in prestamos_a_nd:
        estudiante = persona.objects.get(id=prestamo.id_est)
        nombre = "{} {}".format(estudiante.nombre, estudiante.apellido)
        list_estud.append(nombre)
    return render(request, "gestion_prestamos/buscar_prestamo.html", {'prestamos_a_nd':prestamos_a_nd, 'list_estud':list_estud})

def gestion_sanciones(request):
    return render(request, "gestion_prestamos/gestion_sanciones.html", {})

def generar_sancion(request):
    return render(request, "gestion_prestamos/generar_sancion.html", {})

def visualizar_sanciones(request):
    return render(request, "gestion_prestamos/visualizar_sanciones.html", {})
