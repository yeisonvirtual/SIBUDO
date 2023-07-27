from django.shortcuts import render, redirect
from gestion_recursos.models import libro, trabajo

from authentication.decorators import group_required

# Create your views here.

@group_required(['Estudiante'])
def buscar_libros(request):
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

            elif row == '2':
                # filtra por nombre
                all_libros = libro.objects.filter(nombre__icontains=search)

            elif row == '3':
                # filtra por autor
                all_libros = libro.objects.filter(autor__icontains=search)

            elif row == '4':
                # filtra por anio
                all_libros = libro.objects.filter(anio__icontains=search)

            else:
                # filtra por isbn
                all_libros = libro.objects.filter(isbn__icontains=search)
                
            # retorna los libros filtrados
            return render(request, "recursos/buscar_libros.html", {'nombre':user_name, 'libros': all_libros})
        
        # si el campo de busqueda esta vacio
        else:
            # busca todos los registros
            all_libros = libro.objects.all()

            # retorna todos los libros
            return render(request, "recursos/buscar_libros.html", {'nombre':user_name, 'libros': all_libros})
    
    # si es una consulta de tipo get muestra la plantilla sin la tabla
    return render(request, "recursos/buscar_libros.html", {'nombre':user_name})


@group_required(['Estudiante'])
def buscar_trabajos(request):
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

            if row == '2':
                # filtra por titulo
                all_trabajos = trabajo.objects.filter(titulo__icontains=search)

            if row == '3':
                # filtra por autor
                all_trabajos = trabajo.objects.filter(autor__icontains=search)

            if row == '4':
                # filtra por autor
                all_trabajos = trabajo.objects.filter(palabras_clave__icontains=search)

            if row == '5':
                # filtra por autor
                all_trabajos = trabajo.objects.filter(fecha__icontains=search)
                
            # retorna los libros filtrados
            return render(request, "recursos/buscar_trabajos.html", {'nombre':user_name, 'trabajos': all_trabajos})
        
        # si el campo de busqueda esta vacio
        else:
            # busca todos los registros
            all_trabajos = trabajo.objects.all()

            # retorna todos los libros
            return render(request, "recursos/buscar_trabajos.html", {'nombre':user_name, 'trabajos': all_trabajos})
    
    # si es una consulta de tipo get muestra la plantilla sin la tabla
    return render(request, "recursos/buscar_trabajos.html", {'nombre':user_name})