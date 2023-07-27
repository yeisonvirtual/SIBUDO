from django.shortcuts import render
from authentication.decorators import group_required
from django.contrib.auth.decorators import login_required

@login_required(login_url='/authentication/error_404/')
@group_required(['Director', 'Bibliotecario']) 

def ver_sanciones_estudiante(request):
    return render(request, 'sanciones_estudiante/ver_sanciones_estudiante.html', {})