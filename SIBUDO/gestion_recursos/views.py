from django.shortcuts import render, redirect
from gestion_recursos.forms import formulario_libro, formulario_trabajo
from .models import libro, cantidad_libro, trabajo, cantidad_trabajo

# Create your views here.

def gestion_libros(request):
    user_name = request.user.username

    # si es una consulta de tipo post
    if request.method == "POST":

        # se obtiene el contenido del select
        row = request.POST.get('row')
        # se obtiene el contenido del campo de busqueda
        search = request.POST.get('search')

        # si el campo de busqueda tiene contenido
        if search:

            if row == '1':
                # filtra por id
                all_libros = libro.objects.filter(id=search)

                # recorre todos los filtros y obtiene la cantidad de cada libro
                all_cantidad = []
                for item in all_libros:
                    all_cantidad.append(cantidad_libro.objects.get(libro_id=item.id))

            elif row == '2':
                # filtra por nombre
                all_libros = libro.objects.filter(nombre__icontains=search)

                # recorre todos los filtros y obtiene la cantidad de cada libro
                all_cantidad = []
                for item in all_libros:
                    all_cantidad.append(cantidad_libro.objects.get(libro_id=item.id))

            elif row == '3':
                # filtra por autor
                all_libros = libro.objects.filter(autor__icontains=search)

                # recorre todos los filtros y obtiene la cantidad de cada libro
                all_cantidad = []
                for item in all_libros:
                    all_cantidad.append(cantidad_libro.objects.get(libro_id=item.id))

            elif row == '4':
                # filtra por anio
                all_libros = libro.objects.filter(anio__icontains=search)

                # recorre todos los filtros y obtiene la cantidad de cada libro
                all_cantidad = []
                for item in all_libros:
                    all_cantidad.append(cantidad_libro.objects.get(libro_id=item.id))

            else:
                # filtra por isbn
                all_libros = libro.objects.filter(isbn__icontains=search)

                # recorre todos los filtros y obtiene la cantidad de cada libro
                all_cantidad = []
                for item in all_libros:
                    all_cantidad.append(cantidad_libro.objects.get(libro_id=item.id))
                
            
            # retorna los libros filtrados
            return render(request, "gestion_recursos/gestion_libros.html", {'nombre':user_name, 'libros': all_libros, 'cantidades': all_cantidad})
        
        # si el campo de busqueda esta vacio
        else:
            # busca todos los registros
            all_libros = libro.objects.all()
            all_cantidad = cantidad_libro.objects.all()

            # retorna todos los libros
            return render(request, "gestion_recursos/gestion_libros.html", {'nombre':user_name, 'libros': all_libros, 'cantidades': all_cantidad})
    
    # si es una consulta de tipo get muestra la plantilla sin la tabla
    return render(request, "gestion_recursos/gestion_libros.html", {'nombre':user_name})


def agregar_libro(request):

    form = formulario_libro()

    #si se envia un formulario
    if request.method == "POST":

        form = formulario_libro(data=request.POST)

        if form.is_valid():
            #recupero los datos
            f_nombre = request.POST.get("nombre")
            f_autor = request.POST.get("autor")
            f_edicion = request.POST.get("edicion")
            f_anio = request.POST.get("anio")
            f_isbn = request.POST.get("isbn")
            f_cantidad = request.POST.get("cantidad")

            try:
                # se crea un modelo libro
                libro_nuevo = libro(nombre=f_nombre, autor=f_autor, edicion=f_edicion, anio=f_anio, isbn=f_isbn)
                # se guarda el registro
                libro_nuevo.save()
                # se busca el nuevo libro para obtener el id
                id_nuevo = libro.objects.get(isbn=f_isbn)
                # se crea un modelo cantidad_libro
                c_libro = cantidad_libro(cantidad=f_cantidad, libro=id_nuevo)
                # se guarda el registro
                c_libro.save()

                # limpia el formulario
                form = formulario_libro()

                return render(request, "gestion_recursos/agregar_libro.html", {'form': form, 'valido': 1})
            
            except:
                return redirect("/")

    return render(request, "gestion_recursos/agregar_libro.html", {'form': form})


def eliminar_libro(request, libro_id):

    # se busca el libro por la id
    book = libro.objects.get(id=libro_id)
    # elimina el libro
    book.delete()

    return redirect('Gestion libros')


def editar_libro(request, libro_id):

    # se busca el libro por la id
    book = libro.objects.get(id=libro_id)
    number = cantidad_libro.objects.get(libro=libro_id)

    #si se envia un formulario
    if request.method == "POST":

        form = formulario_libro(data=request.POST)

        if form.is_valid():
            #recupero los datos
            book.nombre = request.POST.get("nombre")
            book.autor = request.POST.get("autor")
            book.edicion = request.POST.get("edicion")
            book.anio = request.POST.get("anio")
            book.isbn = request.POST.get("isbn")
            number.cantidad = request.POST.get("cantidad")

            try:
                # se actualizan los registros
                book.save()
                number.save()

                return render(request, "gestion_recursos/agregar_libro.html", {'form': form, 'valido': 1})
            
            except:
                return redirect("/")
            
    data = {
        'nombre': book.nombre,
        'autor': book.autor,
        'edicion': book.edicion,
        'anio': book.anio,
        'isbn': book.isbn,
        'cantidad': number.cantidad,
    }

    form = formulario_libro(data)
    
    return render(request, "gestion_recursos/agregar_libro.html", {'form': form})


def gestion_trabajos(request):
    user_name = request.user.username

    # si es una consulta de tipo post
    if request.method == "POST":

        # se obtiene el contenido del select
        row = request.POST.get('row')
        # se obtiene el contenido del campo de busqueda
        search = request.POST.get('search')

        # si el campo de busqueda tiene contenido
        if search:

            if row == '1':
                # filtra por id
                all_trabajos = trabajo.objects.filter(id=search)

                # recorre todos los filtros y obtiene la cantidad de cada libro
                all_cantidad = []
                for item in all_trabajos:
                    all_cantidad.append(cantidad_trabajo.objects.get(trabajo_id=item.id))

            if row == '2':
                # filtra por titulo
                all_trabajos = trabajo.objects.filter(titulo__icontains=search)

                # recorre todos los filtros y obtiene la cantidad de cada trabajo
                all_cantidad = []
                for item in all_trabajos:
                    all_cantidad.append(cantidad_trabajo.objects.get(trabajo_id=item.id))

            if row == '3':
                # filtra por autor
                all_trabajos = trabajo.objects.filter(autor__icontains=search)

                # recorre todos los filtros y obtiene la cantidad de cada trabajo
                all_cantidad = []
                for item in all_trabajos:
                    all_cantidad.append(cantidad_trabajo.objects.get(trabajo_id=item.id))

            if row == '4':
                # filtra por autor
                all_trabajos = trabajo.objects.filter(palabras_clave__icontains=search)

                # recorre todos los filtros y obtiene la cantidad de cada trabajo
                all_cantidad = []
                for item in all_trabajos:
                    all_cantidad.append(cantidad_trabajo.objects.get(trabajo_id=item.id))

            if row == '5':
                # filtra por autor
                all_trabajos = trabajo.objects.filter(fecha__icontains=search)

                # recorre todos los filtros y obtiene la cantidad de cada trabajo
                all_cantidad = []
                for item in all_trabajos:
                    all_cantidad.append(cantidad_trabajo.objects.get(trabajo_id=item.id))
                
            # retorna los libros filtrados
            return render(request, "gestion_recursos/gestion_trabajos.html", {'nombre':user_name, 'trabajos': all_trabajos, 'cantidades': all_cantidad})
        
        # si el campo de busqueda esta vacio
        else:
            # busca todos los registros
            all_trabajos = trabajo.objects.all()
            all_cantidad = cantidad_trabajo.objects.all()

            # retorna todos los libros
            return render(request, "gestion_recursos/gestion_trabajos.html", {'nombre':user_name, 'trabajos': all_trabajos, 'cantidades': all_cantidad})
    
    # si es una consulta de tipo get muestra la plantilla sin la tabla
    return render(request, "gestion_recursos/gestion_trabajos.html", {'nombre':user_name})


def agregar_trabajo(request):
    
    form = formulario_trabajo()

    #si se envia un formulario
    if request.method == "POST":

        form = formulario_trabajo(data=request.POST)

        if form.is_valid():
            #recupero los datos
            f_titulo = request.POST.get("titulo")
            f_autor = request.POST.get("autor")
            f_palabras = request.POST.get("palabras_clave")
            f_fecha = request.POST.get("fecha")
            f_cantidad = request.POST.get("cantidad")

            try:
                # se crea un modelo trabajo
                trabajo_nuevo = trabajo(titulo=f_titulo, autor=f_autor, palabras_clave=f_palabras, fecha=f_fecha)
                # se guarda el registro
                trabajo_nuevo.save()
                # se busca el nuevo trabajo para obtener el id
                id_nuevo = trabajo.objects.get(titulo=f_titulo)
                # se crea un modelo cantidad_trabajo
                c_trabajo = cantidad_trabajo(cantidad=f_cantidad, trabajo=id_nuevo)
                # se guarda el registro
                c_trabajo.save()

                # limpia el formulario
                form = formulario_libro()

                return render(request, "gestion_recursos/agregar_trabajo.html", {'form': form, 'valido': 1})
            
            except:
                return redirect("/")


    return render(request, "gestion_recursos/agregar_trabajo.html", {'form': form})


def eliminar_trabajo(request, trabajo_id):

    # se busca el trabajo por la id
    t_grado = trabajo.objects.get(id=trabajo_id)
    # elimina el trabajo
    t_grado.delete()

    return redirect('Gestion trabajos')


def editar_trabajo(request, trabajo_id):

    # se busca el libro por la id
    t_grado = trabajo.objects.get(id=trabajo_id)
    number = cantidad_trabajo.objects.get(trabajo=trabajo_id)
    
    #si se envia un formulario
    if request.method == "POST":

        form = formulario_trabajo(data=request.POST)

        if form.is_valid():
            #recupero los datos
            t_grado.titulo = request.POST.get("titulo")
            t_grado.autor = request.POST.get("autor")
            t_grado.palabras_clave = request.POST.get("palabras_clave")
            t_grado.fecha = request.POST.get("fecha")
            number.cantidad = request.POST.get("cantidad")

            try:
                # se actualizan los registros
                t_grado.save()
                number.save()

                return render(request, "gestion_recursos/agregar_trabajo.html", {'form': form, 'valido': 1})
            
            except:
                return redirect("/")
    
    
    if t_grado.fecha.day>9: day = t_grado.fecha.day
    else: day = f"0{t_grado.fecha.day}"

    if t_grado.fecha.month>9: month = t_grado.fecha.month
    else: month = f"0{t_grado.fecha.month}"

    year = t_grado.fecha.year

    date = f"{year}-{month}-{day}"

    data = {
        'titulo': t_grado.titulo,
        'autor': t_grado.autor,
        'palabras_clave': t_grado.palabras_clave,
        'fecha': date,
        'cantidad': number.cantidad,
    }
    
    form = formulario_trabajo(data)
    
    return render(request, "gestion_recursos/agregar_trabajo.html", {'form': form})