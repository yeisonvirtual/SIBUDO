from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from authentication.decorators import group_required

@login_required

def update_user(request, user_id):
    # Obtener el usuario por su ID
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        # Obtener los datos actualizados del formulario
        user.username = request.POST['username']
        # user.email = request.POST['email']

        # Guardar los cambios en el usuario
        user.save()

        # Redirigir a la página de detalle del usuario actualizado
        context = {
                'active_tab': 'overview',
                'user_id': user.id,
        }
        return render(request, 'authentication/profile/user_profile.html', context)
    
    context = {
        'active_tab': 'overview',
        'user_id': request.user.id,
    }
    return render(request, 'authentication/profile/user_profile.html', context)




