from django.shortcuts import render, redirect

from .forms import Formulario_usuario

from django.core.mail import EmailMessage
# Create your views here.

def gestion_usuarios(request):
    user_name = request.user.username
    return render(request, "gestion_usuarios/gestion_usuarios.html", {'nombre':user_name})

def editar_usuario(request):

    formulario_usuario = Formulario_usuario()

    #si se envia un formulario
    if request.method == "POST":

        formulario_usuario = Formulario_usuario(data=request.POST)

        if formulario_usuario.is_valid():
            #recupero los datos
            cedula = request.POST.get("cedula")
            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido")
            usuario = request.POST.get("usuario")
            rol = request.POST.get("rol")
            estado = request.POST.get("estado")

            try:
                #se envia la palabra 'valido' por la url
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?invalido")
                

    return render(request, "gestion_usuarios/editar_usuario.html", {'miFormulario': formulario_usuario})