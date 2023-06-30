from django.shortcuts import render

# Create your views here.

def gestion_libros(request):
    user_name = request.user.username
    return render(request, "gestion_recursos/gestion_libros.html", {'nombre':user_name})

def gestion_tesis(request):
    user_name = request.user.username
    return render(request, "gestion_recursos/gestion_tesis.html", {'nombre':user_name})