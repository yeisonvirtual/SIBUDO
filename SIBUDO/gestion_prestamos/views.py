from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from .models import Prestamo
from .models import Recurso_Disponible
from gestion_usuarios.models import persona
from gestion_recursos.models import libro
from gestion_recursos.models import cantidad_libro
from gestion_recursos.models import trabajo
from gestion_recursos.models import cantidad_trabajo
from .forms import DatePicker

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
        mi_cantidad = cantidad_libro.objects.get(libro_id=mi_prestamo.id_recurso)
        mi_disponibilidad = Recurso_Disponible.objects.get(Q(tipo_recurso=1) & Q(id_recurso=mi_prestamo.id_recurso))

    if mi_prestamo.tipo_recurso == 2:
        mi_recurso = trabajo.objects.get(id=mi_prestamo.id_recurso)
        mi_cantidad = cantidad_trabajo.objects.get(trabajo_id=mi_prestamo.id_recurso)
        mi_disponibilidad = Recurso_Disponible.objects.get(Q(tipo_recurso=2) & Q(id_recurso=mi_prestamo.id_recurso))
    
    if request.method == "POST":
        # Aumentando en 1 la disponibilidad en la bdd
        try:
            if mi_disponibilidad.n_disponibles + 1 <= mi_cantidad.cantidad:
                mi_disponibilidad.n_disponibles += 1
        except:
            return redirect('/Error/1/')
        
        # Cambiando el estado del estudiante de inactivo a activo
        try:
            if mi_persona.estado != 1:
                mi_persona.estado = 1
        except:
            return redirect('/Error/2/')

        # Cambiando el estado del prestamo a inactivo
        try:
            if mi_prestamo.estado_prestamo != 2:
                mi_prestamo.estado_prestamo = 2
        except:
            return redirect('/Error/3/')
        
        # Almacenando los datos si hasta el momento no ha habido algún inconveniente
        try:
            mi_disponibilidad.save()
            mi_persona.save()
            mi_prestamo.save()
        except:
            return redirect('/Error/4/')
        
        # Si toda la operacion resulta exitosa se retorna esta vista
        return render(request, "gestion_prestamos/prestamo_recibido.html", {})
    
    return render(request, "gestion_prestamos/recibir_prestamo.html", {'mi_prestamo':mi_prestamo, 'mi_persona':mi_persona, 'mi_recurso':mi_recurso})

def prestamo_recibido(request, id_prestamo):
    return render(request, "gestion_prestamos/prestamo_recibido.html", {})

def editar_prestamo(request, id_prestamo):
    # Obteniendo los modelos que se van a utilizar
    mi_prestamo = Prestamo.objects.get(id=id_prestamo)
    mi_persona = persona.objects.get(id=mi_prestamo.id_est)

    if mi_prestamo.tipo_recurso == 1:
        mi_recurso = libro.objects.get(id=mi_prestamo.id_recurso)
    if mi_prestamo.tipo_recurso == 2:
        mi_recurso = trabajo.objects.get(id=mi_prestamo.id_recurso)

    dev_date = str(mi_prestamo.fecha_devolucion)
    mi_date_form = DatePicker(request.POST)
    if request.method == 'POST':
        mi_date_form = DatePicker(request.POST)
        if mi_date_form.is_valid():
            print(request.POST)
        try:
            new_date = request.POST.get('new_date')
            print('Mi fecha recuperada del formulario es:')
            print(new_date)
        except:
            return redirect('/Error/')

    return render(request, "gestion_prestamos/editar_prestamo.html", {'mi_date_form': mi_date_form, 'mi_prestamo':mi_prestamo, 'mi_persona':mi_persona, 'mi_recurso':mi_recurso, 'dev_date':dev_date})

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
        disp_a_prest = Recurso_Disponible.objects.get(Q(tipo_recurso=prestamo.tipo_recurso) & Q(id_recurso=prestamo.id_recurso))
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
