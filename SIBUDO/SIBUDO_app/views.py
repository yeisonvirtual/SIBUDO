from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SIBUDO_app.forms import register_user_form


from django.http import response
from django.http import HttpResponse
# Create your views here.

def index(request):
    user_name = request.user.username
    return render(request, "SIBUDO_app/index.html", {'nombre': user_name})

def not_fount(request):
    return render(request, "SIBUDO_app/not_fount.html")

@api_view(['POST', 'GET'])
def register_user(request):
    
    #if request.method == 'POST':
    if request.method == 'POST' or request.method == 'GET':
        form = register_user_form(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            date_of_birth = form.cleaned_data['date_of_birth']
            gender = form.cleaned_data['gender']
            
            # Realizar la lógica de registro de usuario aquí
            # Por ejemplo, puedes crear una instancia de tu modelo de Usuario y guardarla en la base de datos
            
            # Devolver una respuesta exitosa
            return render(request, "SIBUDO_app/thanks.html")
        else:
            # Devolver una respuesta de error si el formulario no es válido
            my_form = register_user_form()
        return render(request, "SIBUDO_app/register_form.html", {"form": my_form})

