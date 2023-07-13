from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

@login_required
# def profile_view(request):
#     user = request.user
#     #user_role = request.user.userprofile.role
#     return render(request, "user_profile/profile.html", {"name":user})#, 'role': user_role})

def user_profile(request, user_id, active_tab=None):
    # Obtener el usuario por su ID
    user = get_object_or_404(User, id=user_id)
    context = {
                'active_tab': active_tab,
                'user': user,
            }
    return render(request, 'user_profile/user_profile.html', context)

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
        return render(request, 'user_profile/user_profile.html', context)
    
    context = {
        'active_tab': 'overview',
        'user_id': request.user.id,
    }
    return render(request, 'user_profile/user_profile.html', context)







# def delete_user(request, user_id):
#     # Obtener el usuario por su ID
#     user = get_object_or_404(User, id=user_id)

#     if request.method == 'POST':
#         # Eliminar el usuario
#         user.delete()

#         # Redirigir a la página principal o a otra vista
#         return redirect('home')

#     return render(request, 'user_profile.html', {'user': user})
