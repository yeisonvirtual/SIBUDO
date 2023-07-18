from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import Group

#from django.http import HttpResponse

class register_user(View):
    def get(self, request):
        form = UserCreationForm()
        rol_aviable = ['Estudiante', 'Bibliotecario']
        context = {
            'form' : form,
            'rol_aviable' : rol_aviable
        }
        return render(request, "authentication/register.html",context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        rol_aviable = ['Estudiante', 'Bibliotecario']
        context = {
            'form' : form,
            'rol_aviable' : rol_aviable
        }
        if form.is_valid():
            usuario = form.save()
            selected_role = request.POST['role']

            if selected_role == 'Estudiante':

                # Obtén o crea el grupo
                group, created = Group.objects.get_or_create(name='Estudiantes')
                # Asignar al grupo 
                usuario.groups.add(group)
                messages.success(request, 'Registro exitoso')

            elif selected_role == 'Bibliotecario':

                # Obtén o crea el grupo 
                group, created = Group.objects.get_or_create(name='Bibliotecario')
                # Asignar al grupo
                usuario.groups.add(group)
                messages.success(request, 'Registro exitoso')

            # login(request, usuario)
            return render(request, "authentication/register.html",context)
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "authentication/register.html",context)
        
def sign_off(request):
    logout(request)
    return redirect('/')

def sing_in(request):
    if request.method=="POST" : 
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("username")
            password_user = form.cleaned_data.get("password")
            user=authenticate(username = name_user, password=password_user)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Verifique los datos y vuelva a intentar")
        else:
            messages.error(request, "Verifique los datos y vuelva a intentar")

    form = AuthenticationForm()
    context = {
        'form': form,
        # 'messages': messages.get_messages(request),
    }
    return render(request, "authentication/login/login.html", context)
        