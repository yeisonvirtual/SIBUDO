from django.shortcuts import render, get_object_or_404
from ..models import Persona
from django.contrib.auth.models import User, Group

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
        persona = Persona.objects.filter(user=user).first()
        if persona:
            # Combine the user and persona data into a dictionary
            user_info = {
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'cedula': persona.cedula,
                'nombre': persona.nombre,
                'apellido': persona.apellido,
                'rol': user.groups.first().name if user.groups.exists() else None,
                'estado': 'Activo' if persona.estado else 'Inactivo',
            }
            user_data.append(user_info)

    context = {
        'user_data': user_data,
        'groups': groups
    }

    return render(request, "user_management/user_table.html", context)
