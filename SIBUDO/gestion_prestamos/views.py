from django.shortcuts import render
from django.db.models import Q
from .models import Prestamo
from .models import Disponible_a_Prestamo
from gestion_usuarios.models import persona
from gestion_recursos.models import libro
from gestion_recursos.models import trabajo

# Create your views here.
def prestamos(request):
    return render(request, "gestion_prestamos/prestamos.html", {})

def gestion_prestamos(request):
    return render(request, "gestion_prestamos/gestion_prestamos.html", {})

def generar_prestamo(request):
    return render(request, "gestion_prestamos/generar_prestamo.html", {})

def guardar_prestamo(request):
    return render(request, "gestion_prestamos/guardar_prestamo.html", {})

def recibir_prestamo(request,id_prestamo):
    mi_prestamo = Prestamo.objects.get(id=id_prestamo)
    mi_persona = persona.objects.get(id=mi_prestamo.id_est)
    if mi_prestamo.tipo_recurso == 1:
        mi_recurso = libro.objects.get(id=mi_prestamo.id_recurso)
    else:
        mi_recurso = trabajo.objects.get(id=mi_prestamo.id_recurso)
    return render(request, "gestion_prestamos/recibir_prestamo.html", {'mi_prestamo':mi_prestamo, 'mi_persona':mi_persona, 'mi_recurso':mi_recurso})

def prestamo_recibido(request, id_prestamo):
    return render(request, "gestion_prestamos/prestamo_recibido.html", {'id_prestamo':id_prestamo})

def editar_prestamo(request):
    return render(request, "gestion_prestamos/editar_prestamo.html", {})

def buscar_prestamo(request):
    prestamos_a_nd = Prestamo.objects.filter(Q(estado_prestamo=1) | Q(estado_prestamo=2) | Q(estado_prestamo=3))
    list_estud = [None]
    list_tipo_p = [None]
    for prestamo in prestamos_a_nd:
        # Nombres estudiantes
        estudiante = persona.objects.get(id=prestamo.id_est)
        nombre = "{} {}".format(estudiante.nombre, estudiante.apellido)
        list_estud.append(nombre)

        # Tipo de prestamos
        disp_a_prest = Disponible_a_Prestamo.objects.get(Q(tipo_recurso=prestamo.tipo_recurso) & Q(id_recurso=prestamo.id_recurso))
        if disp_a_prest.tipo_prestamo == True:
            list_tipo_p.append('Externo')
        else:
            list_tipo_p.append('Interno')
    return render(request, "gestion_prestamos/buscar_prestamo.html", {'prestamos_a_nd':prestamos_a_nd, 'list_estud':list_estud, 'list_tipo_p':list_tipo_p})

def gestion_sanciones(request):
    return render(request, "gestion_prestamos/gestion_sanciones.html", {})

def generar_sancion(request):
    return render(request, "gestion_prestamos/generar_sancion.html", {})

def visualizar_sanciones(request):
    return render(request, "gestion_prestamos/visualizar_sanciones.html", {})
