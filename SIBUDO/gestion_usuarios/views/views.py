from django.shortcuts import render
from ..models import persona
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from authentication.decorators import group_required

@login_required(login_url='/authentication/error_404/')
@group_required(['Director']) 

def user_table(request):
    users = User.objects.all()
    groups = ['Estudiante', 'Bibliotecario','Invitado']
    # Create a list to store combined user and persona data
    user_data = []

    if request.method == 'POST':

        user_id = request.POST.get('user_id')
        selected_role = request.POST.get('role')
        if selected_role in groups:
            user = User.objects.get(id=user_id)
            group, created = Group.objects.get_or_create(name=selected_role)
        

            if group:
                user.groups.set([group])

    for user in users:
        # Fetch the corresponding Persona instance for each user (assuming one-to-one relationship)
        person = persona.objects.filter(user=user).first()
        if person:
            # Combine the user and persona data into a dictionary
            user_info = {
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'cedula': person.cedula,
                'nombre': person.nombre,
                'apellido': person.apellido,
                'rol': user.groups.first().name if user.groups.exists() else None,
                'estado': 'Activo' if person.estado else 'Inactivo',
            }
            user_data.append(user_info)

    context = {
        'user_data': user_data,
        'groups': [''] + groups
    }

    return render(request, "gestion_usuarios/user_table.html", context)
