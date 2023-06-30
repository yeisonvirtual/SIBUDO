from django.shortcuts import render

# Create your views here.

def gestion_usuarios(request):
    user_name = request.user.username
    return render(request, "gestion_usuarios/gestion_usuarios.html", {'nombre':user_name})