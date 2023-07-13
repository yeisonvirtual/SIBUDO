from django.shortcuts import render, redirect
from gestion_recursos.forms import formulario_libro
from .models import libro, cantidad_libro

# Create your views here.

def gestion_libros(request):
    user_name = request.user.username
    all_libros = libro.objects.all()
    all_cantidad = cantidad_libro.objects.all()
    return render(request, "gestion_recursos/gestion_libros.html", {'nombre':user_name, 'libros': all_libros, 'cantidades': all_cantidad})

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
                id_nuevo = libro.objects.get(nombre=f_nombre, autor=f_autor, edicion=f_edicion, anio=f_anio, isbn=f_isbn)
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