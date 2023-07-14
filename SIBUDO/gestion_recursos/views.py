from django.shortcuts import render, redirect
from gestion_recursos.forms import formulario_libro
from .models import libro, cantidad_libro

# Create your views here.

def gestion_libros(request):
    user_name = request.user.username
    # se obtiene el contenido del campo de busqueda
    seach = request.POST.get('seach')

    # si es una consulta de tipo post
    if request.method == "POST":
        # si el campo de busqueda tiene contenido
        if seach:
            # filtra por nombre
            all_libros = libro.objects.filter(nombre__icontains=seach)

            # recorre todos los filtros y obtiene la cantidad de cada libro
            all_cantidad = []
            for item in all_libros:
                all_cantidad.append(cantidad_libro.objects.get(id=item.id))
                
            #print(all_cantidad[0].id)
            print(all_libros)

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


def gestion_trabajos(request):
    user_name = request.user.username
    return render(request, "gestion_recursos/gestion_trabajos.html", {'nombre':user_name})


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
                # se creo un modelo libro
                libro_nuevo = libro(nombre=f_nombre, autor=f_autor, edicion=f_edicion, anio=f_anio, isbn=f_isbn)
                # se guarda el registro
                libro_nuevo.save()
                # se busca el nuevo libro para obtener el id
                id_nuevo = libro.objects.get(isbn=f_isbn)
                # se creo un modelo cantidad_libro
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

                # limpia el formulario
                #form = formulario_libro()

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

    #form = formulario_libro(nombre=book.nombre, autor=book.autor, edicion=book.edicion,anio=book.anio,isbn=book.isbn,cantidad=number.cantidad)

    form = formulario_libro(data)
    
    return render(request, "gestion_recursos/agregar_libro.html", {'form': form})