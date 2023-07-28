from django.shortcuts import render
from authentication.decorators import group_required
from django.contrib.auth.decorators import login_required
from gestion_usuarios.models import persona
from django.contrib.auth.models import User
from gestion_prestamos.models import Prestamo
from gestion_prestamos.models import Sancion

@login_required(login_url='/authentication/error_404/')
@group_required(['Estudiante']) 
def ver_sanciones_estudiante(request):
    user_id = request.user.id
    # user_profile = User(id=user_id)
    # person_profile = persona.objects.get(user=user_profile)

    historico_prestamos = Prestamo.objects.filter(id_est=user_id)
    list_sanciones = [None]

    for prestamo in historico_prestamos:
        try:
            sancion_encontrada = Sancion.objects.get(id_prestamo=prestamo.id)
            list_sanciones.append(sancion_encontrada)
        except Sancion.DoesNotExist:
            pass

    return render(request, 'sanciones_estudiante/ver_sanciones_estudiante.html', {'list_sanciones':list_sanciones})