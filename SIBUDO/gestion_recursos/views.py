from django.shortcuts import render, redirect
from gestion_recursos.forms import formulario_libro

# Create your views here.

def gestion_libros(request):
    user_name = request.user.username
    return render(request, "gestion_recursos/gestion_libros.html", {'nombre':user_name})

def gestion_trabajos(request):
    user_name = request.user.username
    return render(request, "gestion_recursos/gestion_trabajos.html", {'nombre':user_name})

def agregar_libro(request):

    form = formulario_libro()

    #si se envia un formulario
    if request.method == "POST":

        formulario_libro = formulario_libro(data=request.POST)

        if form.is_valid():
            #recupero los datos
            nombre = request.POST.get("nombre")
            autor = request.POST.get("autor")
            edicion = request.POST.get("edicion")
            anio = request.POST.get("anio")
            isbn = request.POST.get("isbn")

            try:
                #se envia la palabra 'valido' por la url
                return redirect("libros/agregar")
            except:
                return redirect("libros/agregar")
                

    return render(request, "gestion_recursos/agregar_libro.html", {'form': form})