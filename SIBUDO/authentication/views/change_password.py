from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def change_password_api(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Actualiza la sesión de autenticación del usuario
            messages.success(request, 'Contraseña cambiada exitosamente.')
            
            context = {
                'active_tab': 'change_password',
                'user_id': request.user.id,
            }
            return render(request, 'authentication/profile/user_profile.html', context)  # Renderiza la plantilla de perfil del usuario

        else:
            for field, error_list in form.errors.items():
                for error in error_list:
                    messages.error(request, f'{error}')
    
    context = {
        'active_tab': 'change_password', # Lógica para determinar qué pestaña debe estar activa
        'user_id': request.user.id,
    }
    return render(request, 'authentication/profile/user_profile.html', context)  # Renderiza la plantilla de perfil del usuario
