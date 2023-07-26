from django.shortcuts import render
from django.views.generic import View
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from gestion_usuarios.forms import User_form, Persona_Form 

class register_user(View):
    def get(self, request):
        user_form = User_form()
        person_form = Persona_Form()
        rol_aviable = ['Estudiante', 'Bibliotecario', 'Invitado']
        context = {
            'user_form' : user_form,
            'person_form' : person_form,
            'rol_aviable' : rol_aviable,
        }
        return render(request, "gestion_usuarios/register/register.html",context)

    def post(self, request):
        user_form = User_form(request.POST)
        person_form = Persona_Form(request.POST)
        rol_aviable = ['Estudiante', 'Bibliotecario']
        context = {
            'user_form' : user_form,
            'person_form' : person_form,
            'rol_aviable' : rol_aviable,
        }
        if user_form.is_valid() and person_form.is_valid():
            print("entrooooooooooooooooooooooooooooo")
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

            if selected_role == 'Estudiante':

                # Obtén o crea el grupo
                group, created = Group.objects.get_or_create(name='Estudiantes')
                # Asignar al grupo 
                user.groups.add(group)
                messages.success(request, 'Registro exitoso')

            elif selected_role == 'Bibliotecario':

                # Obtén o crea el grupo 
                group, created = Group.objects.get_or_create(name='Bibliotecario')
                # Asignar al grupo
                user.groups.add(group)
                messages.success(request, 'Registro exitoso')

            return render(request, "gestion_usuarios/register/register.html",context)
        else:
            return render(request, "gestion_usuarios/register/register.html",context)
        