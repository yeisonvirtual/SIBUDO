from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from gestion_usuarios.models import Persona

@csrf_exempt
def change_password_api(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        #informacino necesaria para agreagar al contexto
        user_profile = get_object_or_404(User, id=request.user.id)
        try:
            person_profile = Persona.objects.get(user=user_profile)
        except Persona.DoesNotExist:
            pass


        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Actualiza la sesión de autenticación del usuario
            messages.success(request, 'Contraseña cambiada exitosamente.')
            
            context = {
                'active_tab': 'change_password',
                'user_id': request.user.id,
                'user_profile': user_profile,
                'person_profile': person_profile,
            }
            return render(request, 'authentication/profile/user_profile.html', context)  # Renderiza la plantilla de perfil del usuario

        else:
            for field, error_list in form.errors.items():
                for error in error_list:
                    messages.error(request, f'{error}')
    
    context = {
        'active_tab': 'change_password', # Lógica para determinar qué pestaña debe estar activa
        'user_id': request.user.id,
        'user_profile': user_profile,
        'person_profile': person_profile,
    }
    return render(request, 'authentication/profile/user_profile.html', context)  # Renderiza la plantilla de perfil del usuario
