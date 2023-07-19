from django.shortcuts import render
from datetime import date, datetime
from django.db.models import Q
from .models import Prestamo
from .models import Recurso_Disponible
from .models import Sancion
from gestion_usuarios.models import persona
from gestion_recursos.models import libro
from gestion_recursos.models import cantidad_libro
from gestion_recursos.models import trabajo
from gestion_recursos.models import cantidad_trabajo
from .forms import DatePicker, Penalty_DatePicker

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
            titulo = 'Error'
            sub_titulo = 'Ha ocurrido un error al intentar modificar la disponibilidad del recurso'
            mensaje = 'Vuelva a intentarlo y si el problema persiste comuníquese con servicio técnico'
            icon = 2
            return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
        
        # Cambiando el estado del estudiante de inactivo a activo
        try:
            if mi_persona.estado != 1:
                mi_persona.estado = 1
        except:
            titulo = 'Error'
            sub_titulo = 'Ha ocurrido un error al intentar modificar el estado del estudiante'
            mensaje = 'Vuelva a intentarlo y si el problema persiste comuníquese con servicio técnico'
            icon = 2
            return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})

        # Cambiando el estado del prestamo a inactivo
        try:
            if mi_prestamo.estado_prestamo != 2:
                mi_prestamo.estado_prestamo = 2
        except:
            titulo = 'Error'
            sub_titulo = 'Ha ocurrido un error al intentar modificar el prestamo'
            mensaje = 'Vuelva a intentarlo y si el problema persiste comuníquese con servicio técnico'
            icon = 2
            return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
        
        # Almacenando los datos si hasta el momento no ha habido algún inconveniente
        try:
            mi_disponibilidad.updated = datetime.now()
            mi_disponibilidad.save()

            mi_persona.updated = datetime.now()
            mi_persona.save()

            mi_prestamo.updated = datetime.now()
            mi_prestamo.save()
        except:
            titulo = 'Error'
            sub_titulo = 'Ha ocurrido un error al intentar guardar los datos'
            mensaje = 'Vuelva a intentarlo y si el problema persiste comuníquese con servicio técnico'
            icon = 2
            return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
        
        # Si toda la operacion resulta exitosa se retorna esta vista
        titulo = 'Prestamo Recibido'
        sub_titulo = 'Prestamo Recibido Exitosamente'
        mensaje = 'En breves segundos se verá reflejado en el sistema'
        icon = 1
        return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
    
    return render(request, "gestion_prestamos/recibir_prestamo.html", {'mi_prestamo':mi_prestamo, 'mi_persona':mi_persona, 'mi_recurso':mi_recurso})

def mensaje_resultado(request, id_prestamo):
    titulo = ''
    sub_titulo = ''
    mensaje = ''
    icon = 0
    return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})

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
            try:
                new_date = request.POST.get('new_date')
                mi_prestamo.fecha_devolucion = new_date
                mi_prestamo.updated = datetime.now()
                mi_prestamo.save()
                titulo = 'Prestamo Modificado'
                sub_titulo = 'Prestamo Modificado Exitosamente'
                mensaje = 'En breves segundos se verá reflejado en el sistema'
                icon = 1
                return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
            except:
                titulo = 'Error'
                sub_titulo = 'Ha ocurrido un error al intentar modificar la fecha'
                mensaje = 'Vuelva a intentarlo y si el problema persiste comuníquese con servicio técnico'
                icon = 2
                return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})

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

        # Tipos de prestamos
        disp_a_prest = Recurso_Disponible.objects.get(Q(tipo_recurso=prestamo.tipo_recurso) & Q(id_recurso=prestamo.id_recurso))
        if disp_a_prest.tipo_prestamo == True:
            list_tipo_p.append('Externo')
        else:
            list_tipo_p.append('Interno')
    return render(request, "gestion_prestamos/buscar_prestamo.html", {'prestamos_a_nd':prestamos_a_nd, 'list_estud':list_estud, 'list_tipo_p':list_tipo_p})

def gestion_sanciones(request):
    return render(request, "gestion_prestamos/gestion_sanciones.html", {})

def generar_sancion(request):
    elegibles_a_sancion = Prestamo.objects.filter(estado_prestamo=3)
    list_estud = [None]
    list_tipo_p = [None]
    for prestamo in elegibles_a_sancion:
        #Nombres estudiantes
        estudiante = persona.objects.get(id=prestamo.id_est)
        nombre = '{} {}'.format(estudiante.nombre, estudiante.apellido)
        list_estud.append(nombre)

        #Tipos de prestamos
        disp_a_prestamo = Recurso_Disponible.objects.get(Q(tipo_recurso=prestamo.tipo_recurso) & Q(id_recurso=prestamo.id_recurso))
        if disp_a_prestamo == True:
            list_tipo_p.append('Externo')
        else:
            list_tipo_p.append('Interno')
        
    return render(request, "gestion_prestamos/generar_sancion.html", {'elegibles_a_sancion':elegibles_a_sancion, 'list_estud':list_estud, 'list_tipo_p':list_tipo_p})

def sancionar(request, id_prestamo):
    # Método GET
    # Obteniendo los datos para poder generar la sancion
    mi_prestamo = Prestamo.objects.get(id=id_prestamo)
    mi_persona = persona.objects.get(id=mi_prestamo.id_est)

    if mi_prestamo.tipo_recurso == 1:
        mi_recurso = libro.objects.get(id=mi_prestamo.id_recurso)
    if mi_prestamo.tipo_recurso == 2:
        mi_recurso = trabajo.objects.get(id=mi_prestamo.id_recurso)
    
    # Obteniendo la fecha actual en la que se generará la sanción
    today = date.today()

    # Creando el datepicker para mostrar mientras GET
    penalty_date_form = Penalty_DatePicker(request.POST)

    # Método POST
    if request.method == 'POST':
        # Crando datepicker para capturar datos del form
        penalty_date_form = Penalty_DatePicker(request.POST)
        if penalty_date_form.is_valid():

            # Creando la sancion
            try:
                # Rescatando el valor de la fecha final de penalizacion
                culminacion = request.POST.get('penalty_date')

                # Creando la sancion
                ns_prestamo = mi_prestamo.id
                ns_estado = 1
                ns_aplicacion = date.today()
                ns_culminacion = culminacion
                ns_created = datetime.now()
                ns_updated = datetime.now()
                mi_sancion = Sancion(id_prestamo=ns_prestamo, estado=ns_estado, fecha_aplicacion=ns_aplicacion, fecha_culminacion=ns_culminacion, created=ns_created, updated=ns_updated)
            except:
                titulo = 'Error'
                sub_titulo = 'Ha ocurrido un error al intentar generar la sanción'
                mensaje = 'Vuelva a intentarlo y si el problema persiste comuníquese con servicio técnico'
                icon = 2
                return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
            
            # Aumentando la disponibilidad del recurso
            try:
                disponibilidad = Recurso_Disponible.objects.get(Q(tipo_recurso=mi_prestamo.tipo_recurso) & Q(id_recurso=mi_prestamo.id_recurso))
                if mi_prestamo.tipo_recurso == 1:
                    # Es un libro
                    recurso = cantidad_libro.objects.get(libro_id=mi_prestamo.id_recurso)
                elif mi_prestamo.tipo_recurso == 2:
                    # Es un trabajo de grado
                    recurso = cantidad_trabajo.objects.get(trabajo_id=mi_prestamo.id_recurso)

                if ((disponibilidad.n_disponibles + 1) <= (recurso.cantidad)):
                    disponibilidad.n_disponibles += 1
            except:
                titulo = 'Error'
                sub_titulo = 'Ha ocurrido un error al intentar aumentar la disponibilidad del recurso'
                mensaje = 'Vuelva a intentarlo y si el problema persiste comuníquese con servicio técnico'
                icon = 2
                return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})

            # Cambiando el estado del prestamo
            try:
                if mi_prestamo.estado_prestamo != 2:
                    mi_prestamo.estado_prestamo = 2
            except:
                titulo = 'Error'
                sub_titulo = 'Ha ocurrido un error al intentar cambiar el estado del prestamo'
                mensaje = 'Vuelva a intentarlo y si el problema persiste comuníquese con servicio técnico'
                icon = 2
                return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})

            # Guardando los cambios realizados
            try:
                # pass

                # Guardando la sanción
                mi_sancion.save()

                # Guardando la disponibilidad
                disponibilidad.updated = datetime.now()
                disponibilidad.save()


                # Guardando la modificación al prestamo
                mi_prestamo.updated = datetime.now()
                mi_prestamo.save()


                # Redirigiendo a mensaje de éxito
                titulo = 'Sanción Aplicada'
                sub_titulo = 'La sanción se ha aplicado correctamente'
                mensaje = 'En breves segundos se verá reflejada en el sistema'
                icon = 1
                return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
            except:
                titulo = 'Error'
                sub_titulo = 'Ha ocurrido un error al intentar guardar la sanción'
                mensaje = 'Vuelva a intentarlo y si el problema persiste comuníquese con servicio técnico'
                icon = 2
                return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
    
    # Se retorna la vista del método GET
    return render(request, "gestion_prestamos/sancionar.html", {"mi_prestamo":mi_prestamo, "mi_persona":mi_persona, "mi_recurso":mi_recurso, "today":today, 'penalty_date_form':penalty_date_form})

def visualizar_sanciones(request):

    #listas que ayudan a mostrar datos en el front
    list_estud = [None]
    list_tipo_p = [None]

    # Obteniendo las sanciones activas
    sanciones = Sancion.objects.filter(Q(estado=1))

    # Obteniendo los prestamos y estudiantes sancionados
    for prestamo in sanciones:
        prestamo_sancionado = Prestamo.objects.get(id=prestamo.id_prestamo)
        estudiante_sancionado = persona.objects.get(id=prestamo_sancionado.id_est)

        # Agregando el nombre de los estudiantes a la lista
        nombre = '{} {}'.format(estudiante_sancionado.nombre, estudiante_sancionado.apellido)
        list_estud.append(nombre)

        # Agregando los tipos de prestamos a la lista
        # Tipos de prestamos
        disp_a_prest = Recurso_Disponible.objects.get(Q(tipo_recurso=prestamo_sancionado.tipo_recurso) & Q(id_recurso=prestamo_sancionado.id_recurso))
        if disp_a_prest.tipo_prestamo == True:
            list_tipo_p.append('Externo')
        else:
            list_tipo_p.append('Interno')
    
    return render(request, "gestion_prestamos/visualizar_sanciones.html", {'sanciones':sanciones, 'list_estud':list_estud, 'list_tipo_p':list_tipo_p})
