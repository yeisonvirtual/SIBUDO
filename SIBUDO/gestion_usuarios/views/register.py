from django.shortcuts import render
# from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from gestion_usuarios.forms import User_form, Persona_Form 
from authentication.decorators import group_required
from django.contrib.auth.decorators import login_required

@login_required(login_url='/authentication/error_404/')
@group_required(['Director']) 

def register_user(request): 
    if request.method == 'POST':

        user_form = User_form(request.POST)
        person_form = Persona_Form(request.POST)
        rol_aviable = ['Estudiante', 'Bibliotecario', 'Invitado']
        context = {
            'user_form' : user_form,
            'person_form' : person_form,
            'rol_aviable' : rol_aviable,
        }
        if user_form.is_valid() and person_form.is_valid():

            user = user_form.save(commit=False)
            # se obtienen los valores de los campos adicionales
            first_name = request.POST.get('nombre')
            last_name = request.POST.get('apellido')
            email = request.POST.get('correo')
            # # Asigna los campos adicionales al usuario
            user.first_name = first_name
            user.last_name = last_name
            user.email = email

            user.save()

            person = person_form.save(commit=False)
            person.user = user
            # person.fechafecha_nacimiento = request.POST.get('nombre')
            person.save()

            selected_role = request.POST['role']

            # Obtén o crea el grupo 
            group, created = Group.objects.get_or_create(name=selected_role)
            # Asignar al grupo
            user.groups.add(group)
            messages.success(request, 'Registro exitoso')

            return render(request, "gestion_usuarios/register/register.html",context)
        else:
            return render(request, "gestion_usuarios/register/register.html",context)
    else:
        user_form = User_form()
        person_form = Persona_Form()
        rol_aviable = ['Estudiante', 'Bibliotecario', 'Invitado']
        context = {
            'user_form' : user_form,
            'person_form' : person_form,
            'rol_aviable' : rol_aviable,
        }
        return render(request, "gestion_usuarios/register/register.html",context)  