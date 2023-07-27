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
from .forms import DatePicker, Penalty_DatePicker, CI_Form, Selector_Recurso_Form
from .estudiante import Estudiante
from authentication.decorators import group_required
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/authentication/error_404/')
@group_required(['Director', 'Bibliotecario'])
def prestamos(request):
    return render(request, "gestion_prestamos/prestamos.html", {})

@login_required(login_url='/authentication/error_404/')
@group_required(['Director', 'Bibliotecario'])
def gestion_prestamos(request):
    return render(request, "gestion_prestamos/gestion_prestamos.html", {})

@login_required(login_url='/authentication/error_404/')
@group_required(['Director', 'Bibliotecario'])
def generar_prestamo(request):
    estudiante = Estudiante(request)
    ci_form = CI_Form(request.POST)
    hay_estudiante = 0
    mi_estudiante = 0
    if request.method == 'POST':
        # Verificando la cedula del estudiante
        if 'verificar' in request.POST:
            ci_form = CI_Form(request.POST)
            if ci_form.is_valid():
                try:
                    ci = request.POST.get('ci')
                    mi_estudiante = persona.objects.get(cedula=ci)
                    estudiante.actualizar(new_estudiante=mi_estudiante)
                    hay_estudiante = 1
                    selector_form = Selector_Recurso_Form(request.POST)
                    tipo_recurso = 1

                    # Si el estudiante se encuentra activo la primera opcion de
                    # recurso será libro, por eso se aprovecha de enviar los
                    # recursos disponibles. Si se quiere trabajo de grado se
                    # puede seleccionar en el form-selector
                    libros_disponibles = Recurso_Disponible.objects.filter(Q(tipo_recurso=1) & Q(n_disponibles__gte=1))
                    list_nombre = [None]
                    list_autor = [None]
                    list_edicion = [None]
                    list_uso = [None]
                    list_anio = [None]
                    list_ISBN = [None]
                    list_estado = [None]
                    list_id = [None]
                    for libro_it in libros_disponibles:
                        libro_a_verificar = libro.objects.get(Q(id=libro_it.id))
                        if libro_a_verificar.disponible == 1:
                            list_nombre.append(libro_a_verificar.nombre)
                            list_autor.append(libro_a_verificar.autor)
                            list_edicion.append(libro_a_verificar.edicion)
                            list_uso.append(libro_it.tipo_prestamo)
                            list_anio.append(libro_a_verificar.anio)
                            list_ISBN.append(libro_a_verificar.isbn)
                            list_estado.append(libro_a_verificar.disponible)
                            list_id.append(libro_a_verificar.id)
                    return render(request, "gestion_prestamos/generar_prestamo.html", {'ci_form':ci_form, 'hay_estudiante':hay_estudiante,'selector_form':selector_form, 'tipo_recurso':tipo_recurso, 'list_nombre':list_nombre, 'list_autor':list_autor, 'list_edicion':list_edicion, 'list_uso':list_uso, 'list_anio':list_anio, 'list_ISBN':list_ISBN, 'list_estado':list_estado, 'list_id':list_id})
                    pass
                except:
                    titulo = 'Error'
                    sub_titulo = 'La persona con la cédula introducida no existe'
                    mensaje = 'De no ser esto cierto comuníquese con servicio técnico'
                    icon = 2
                    return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
            else:
                titulo = 'Error'
                sub_titulo = 'Ha ocurrido un error inesperado'
                mensaje = 'Inténtelo nuevamente y si el problema persiste comuníquese con servicio técnico'
                icon = 2
                return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
        
        # Seleccionando el recurso
        if 'select-recurso' in request.POST:
            selector_form = Selector_Recurso_Form(request.POST)
            if selector_form.is_valid():
                try:
                    eleccion = request.POST.get('selector')
                    if eleccion == '1':
                        try:
                            hay_estudiante = 1
                            selector_form = Selector_Recurso_Form(request.POST)
                            tipo_recurso = 1

                            # Cargando trabajos disponibles
                            libros_disponibles = Recurso_Disponible.objects.filter(Q(tipo_recurso=1) & Q(n_disponibles__gte=1))
                            list_nombre = [None]
                            list_autor = [None]
                            list_edicion = [None]
                            list_uso = [None]
                            list_anio = [None]
                            list_ISBN = [None]
                            list_estado = [None]
                            list_id = [None]
                            for libro_it in libros_disponibles:
                                libro_a_verificar = libro.objects.get(Q(id=libro_it.id))
                                if libro_a_verificar.disponible == 1:
                                    list_nombre.append(libro_a_verificar.nombre)
                                    list_autor.append(libro_a_verificar.autor)
                                    list_edicion.append(libro_a_verificar.edicion)
                                    list_uso.append(libro_it.tipo_prestamo)
                                    list_anio.append(libro_a_verificar.anio)
                                    list_ISBN.append(libro_a_verificar.isbn)
                                    list_estado.append(libro_a_verificar.disponible)
                                    list_id.append(libro_a_verificar.id)
                            return render(request, "gestion_prestamos/generar_prestamo.html", {'ci_form':ci_form, 'hay_estudiante':hay_estudiante,'selector_form':selector_form, 'tipo_recurso':tipo_recurso, 'list_nombre':list_nombre, 'list_autor':list_autor, 'list_edicion':list_edicion, 'list_uso':list_uso, 'list_anio':list_anio, 'list_ISBN':list_ISBN, 'list_estado':list_estado, 'list_id':list_id})
                        except:
                            titulo = 'Error'
                            sub_titulo = 'Ha ocurrido un error inesperado'
                            mensaje = 'hello its mi Inténtelo nuevamente y si el problema persiste comuníquese con servicio técnico'
                            icon = 2
                            return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
                    elif eleccion == '2':
                        try:
                            hay_estudiante = 1
                            selector_form = Selector_Recurso_Form(request.POST)
                            tipo_recurso = 2

                            # Cargando trabajos disponibles
                            trabajos_disponibles = Recurso_Disponible.objects.filter(Q(tipo_recurso=2) & Q(n_disponibles__gte=1))
                            list_titulo = [None]
                            list_autor = [None]
                            list_p_clave = [None]
                            list_uso = [None]
                            list_fecha = [None]
                            list_estado = [None]
                            list_id = [None]
                            for trabajo_it in trabajos_disponibles:
                                trabajo_a_verificar = trabajo.objects.get(Q(id=trabajo_it.id_recurso))
                                if trabajo_a_verificar.disponible == 1:
                                    list_titulo.append(trabajo_a_verificar.titulo)
                                    list_autor.append(trabajo_a_verificar.autor)
                                    list_p_clave.append(trabajo_a_verificar.palabras_clave)
                                    list_uso.append(trabajo_it.tipo_prestamo)
                                    list_fecha.append(trabajo_a_verificar.fecha)
                                    list_estado.append(trabajo_a_verificar.disponible)
                                    list_id.append(trabajo_a_verificar.id)
                            return render(request, "gestion_prestamos/generar_prestamo.html", {'ci_form':ci_form, 'hay_estudiante':hay_estudiante,'selector_form':selector_form, 'tipo_recurso':tipo_recurso, 'list_titulo':list_titulo, 'list_autor':list_autor, 'list_p_clave':list_p_clave, 'list_uso':list_uso, 'list_fecha':list_fecha, 'list_estado':list_estado, 'list_id':list_id})
                        except:
                            titulo = 'Error'
                            sub_titulo = 'Ha ocurrido un error inesperado'
                            mensaje = 'Inténtelo nuevamente y si el problema persiste comuníquese con servicio técnico'
                            icon = 2
                            return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
                    else:
                        titulo = 'Error'
                        sub_titulo = 'La opción seleccionada es inválida'
                        mensaje = 'Inténtelo nuevamente y si el problema persiste comuníquese con servicio técnico'
                        icon = 2
                        return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
                except:
                    titulo = 'Error'
                    sub_titulo = 'Ha ocurrido un error inesperado'
                    mensaje = 'Inténtelo nuevamente y si el problema persiste comuníquese con servicio técnico'
                    icon = 2
                    return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
            else:
                titulo = 'Error'
                sub_titulo = 'Ha ocurrido un error inesperado'
                mensaje = 'Inténtelo nuevamente y si el problema persiste comuníquese con servicio técnico'
                icon = 2
                return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})


    return render(request, "gestion_prestamos/generar_prestamo.html", {'ci_form':ci_form, 'hay_estudiante':hay_estudiante})

@login_required(login_url='/authentication/error_404/')
@group_required(['Director', 'Bibliotecario'])
def guardar_prestamo(request, id_est, tipo_rec, id_rec):
    estudiante = persona.objects.get(id=id_est)
    if tipo_rec == 1:
        recurso = libro.objects.get(id=id_rec)
    elif tipo_rec == 2:
        recurso = trabajo.objects.get(id=id_rec)
    else:
        titulo = 'Error'
        sub_titulo = 'Ha ocurrido un error inesperado'
        mensaje = 'Vuelva a intentarlo y si el problema persiste comuníquese con servicio técnico'
        icon = 2
        return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
    
    disponibilidad = Recurso_Disponible.objects.get(Q(tipo_recurso=tipo_rec) & Q(id_recurso=id_rec))

    datePicker_form = DatePicker(request.POST)
    today = date.today()

    if request.method == 'POST':
        datePicker_form = DatePicker(request.POST)
        if datePicker_form.is_valid():

            # Guardando el prestamo recien creado
            try:
                np_id_est = id_est
                np_tipo_rec = tipo_rec
                np_id_rec = id_rec
                np_fecha_prestamo = date.today()
                np_fecha_devolucion = request.POST.get('new_date')
                np_estado_p = 1
                np_created = datetime.now()
                np_updated = datetime.now()
                mi_prestamo = Prestamo(id_est=np_id_est, tipo_recurso=np_tipo_rec, id_recurso=np_id_rec, fecha_prestamo=np_fecha_prestamo, fecha_devolucion=np_fecha_devolucion, estado_prestamo=np_estado_p, created=np_created, updated=np_updated)
            except:
                titulo = 'Error'
                sub_titulo = 'Ha ocurrido un error al intentar crear el prestamo'
                mensaje = 'Vuelva a intentarlo y si el problema persiste comuníquese con servicio técnico'
                icon = 2
                return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})

            # Disminuyendo la disponibilidad del recurso
            try:
                if ((disponibilidad.n_disponibles - 1) >= 0):
                    disponibilidad.n_disponibles -= 1
                else:
                    raise
            except:
                titulo = 'Error'
                sub_titulo = 'Ha ocurrido un error al intentar disminuir la disponibilidad del recurso'
                mensaje = 'Vuelva a intentarlo y si el problema persiste comuníquese con servicio técnico'
                icon = 2
                return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
        
            try:
                estudiante.estado = 0
            except:
                titulo = 'Error'
                sub_titulo = 'Ha ocurrido un error al intentar cambiar el estado del estudiante'
                mensaje = 'Vuelva a intentarlo y si el problema persiste comuníquese con servicio técnico'
                icon = 2
                return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
        
            try:
                # Guardando prestamo
                mi_prestamo.save()

                # Guardando disponibilidad
                disponibilidad.updated = datetime.now()
                disponibilidad.save()

                # Guardando estudiante
                estudiante.updated = datetime.now()
                estudiante.save()
                
                # Devolviendo vista de exito
                titulo = 'Prestamo guardado'
                sub_titulo = 'Prestamo Guardado Exitosamente'
                mensaje = 'En breves segundos se verá reflejado en el sistema'
                icon = 1
                return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})
            except:
                titulo = 'Error'
                sub_titulo = 'Ha ocurrido un error al intentar guardar los cambios'
                mensaje = 'Vuelva a intentarlo y si el problema persiste comuníquese con servicio técnico'
                icon = 2
                return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})

    return render(request, "gestion_prestamos/guardar_prestamo.html", {'tipo_rec':tipo_rec, 'disponibilidad':disponibilidad, 'recurso':recurso,'today':today, 'datePicker_form':datePicker_form, 'estudiante':estudiante, 'recurso':recurso})

@login_required(login_url='/authentication/error_404/')
@group_required(['Director', 'Bibliotecario'])
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

@login_required(login_url='/authentication/error_404/')
@group_required(['Director', 'Bibliotecario'])
def mensaje_resultado(request, id_prestamo):
    titulo = ''
    sub_titulo = ''
    mensaje = ''
    icon = 0
    return render(request, "gestion_prestamos/mensaje_resultado.html", {'titulo':titulo, 'sub_titulo':sub_titulo, 'mensaje':mensaje, 'icon':icon})

@login_required(login_url='/authentication/error_404/')
@group_required(['Director', 'Bibliotecario'])
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
                mi_prestamo.estado_prestamo = 1
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

@login_required(login_url='/authentication/error_404/')
@group_required(['Director', 'Bibliotecario'])
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

@login_required(login_url='/authentication/error_404/')
@group_required(['Director', 'Bibliotecario'])
def gestion_sanciones(request):
    return render(request, "gestion_prestamos/gestion_sanciones.html", {})

@login_required(login_url='/authentication/error_404/')
@group_required(['Director', 'Bibliotecario'])
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

@login_required(login_url='/authentication/error_404/')
@group_required(['Director', 'Bibliotecario'])
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

@login_required(login_url='/authentication/error_404/')
@group_required(['Director', 'Bibliotecario'])
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