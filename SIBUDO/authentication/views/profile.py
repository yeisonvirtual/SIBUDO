from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from gestion_usuarios.models import persona
from django.contrib.auth.decorators import login_required


@login_required(login_url='/authentication/error_404/')
def user_profile(request, user_id, active_tab='overview'):
    # Obtener el usuario por su ID
    user_profile = get_object_or_404(User, id=user_id)
    user_groups = user_profile.groups.all()

    try:
        person_profile = persona.objects.get(user=user_profile)

        context = {
                'active_tab': active_tab,
                'user_profile': user_profile,
                'person_profile': person_profile,
                'rol_aviable': ['Estudiante', 'Bibliotecario', 'Invitado'],
                'user_groups': user_groups

            }
        return render(request, 'authentication/profile/user_profile.html', context)
    except persona.DoesNotExist:
        pass

    context = {
                'active_tab': active_tab,
                'user_profile': user_profile,
                'rol_aviable': ['Estudiante', 'Bibliotecario', 'Invitado'],
                'user_groups': user_groups
    }
    return render(request, 'authentication/profile/user_profile.html', context)


 