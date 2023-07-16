from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from .models import Prestamo
from .models import Disponible_a_Prestamo
from gestion_usuarios.models import persona
from gestion_recursos.models import libro
from gestion_recursos.models import cantidad_libro
from gestion_recursos.models import trabajo
from gestion_recursos.models import cantidad_trabajo

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
    # Obteniendo los modelos que se van a utilizar
    mi_prestamo = Prestamo.objects.get(id=id_prestamo)
    mi_persona = persona.objects.get(id=mi_prestamo.id_est)
    if mi_prestamo.tipo_recurso == 1:
        mi_recurso = libro.objects.get(id=mi_prestamo.id_recurso)
    else:
        mi_recurso = trabajo.objects.get(id=mi_prestamo.id_recurso)
    
    disposicion = Disponible_a_Prestamo.objects.get(Q(id_recurso=mi_prestamo.id_recurso) & Q(tipo_recurso=mi_prestamo.tipo_recurso))

    if request.method == "POST":
        # Aumentando en 1 la disponibilidad en la bdd
        try:
            # Verificando si el recurso es libro, trabajo o algo mas
            if mi_prestamo.tipo_recurso == 1:
                # obteniendo la cantidad que hay de dicho recurso
                mi_libro = cantidad_libro.objects.get(libro_id=mi_prestamo.id_recurso)
                # verificando que la cantidad de libros sea la indicada
                # a fin de que en disponibles no se exceda la cantidad real de libros
                if ((disposicion.n_disponibles + 1) <= (mi_libro.cantidad)):
                    disposicion.n_disponibles += 1
                else:
                    return redirect('/Error/1/')
            elif mi_prestamo.tipo_recurso == 2:
                mi_trabajo = cantidad_trabajo.objects.get(trabajo_id=mi_prestamo.id_recurso)
                if ((disposicion.n_disponibles + 1) <= (mi_trabajo.cantidad)):
                    disposicion.n_disponibles += 1
                else:
                    return redirect('/Error/2/')
            else:
                return redirect('/Error/3/')
        except:
            return redirect('/Error/4/')
        
        # Cambiando el estado del estudiante de inactivo a activo
        try:
            if mi_persona.estado != 1:
                mi_persona.estado = 1
            else:
                return redirect('/Error/5/')
        except:
            return redirect('/Error/6/')

        # Cambiando el estado del prestamo a inactivo
        try:
            if mi_prestamo != 2:
                mi_prestamo.estado_prestamo = 2
            else:
                return redirect('/Error/7/')
        except:
            return redirect('/Error/8/')

        # Guardando los cambios realizados en todos los modelos
        disposicion.save()
        mi_persona.save()
        mi_prestamo.save()
        
        # Si toda la operacion resulta exitosa se retorna esta vista
        return render(request, "gestion_prestamos/prestamo_recibido.html", {'mi_prestamo':mi_prestamo, 'mi_persona':mi_persona, 'mi_recurso':mi_recurso})
    
    return render(request, "gestion_prestamos/recibir_prestamo.html", {'mi_prestamo':mi_prestamo, 'mi_persona':mi_persona, 'mi_recurso':mi_recurso})

def prestamo_recibido(request, id_prestamo):
    return render(request, "gestion_prestamos/prestamo_recibido.html", {})

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
