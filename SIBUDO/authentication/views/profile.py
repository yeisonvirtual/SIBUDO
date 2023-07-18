from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from authentication.decorators import group_required


@login_required

@group_required(['Director','Invitados']) 
def user_profile(request, user_id, active_tab=None):
    # Obtener el usuario por su ID
    user = get_object_or_404(User, id=user_id)
    context = {
                'active_tab': active_tab,
                'user': user,
            }
    return render(request, 'authentication/profile/user_profile.html', context)


