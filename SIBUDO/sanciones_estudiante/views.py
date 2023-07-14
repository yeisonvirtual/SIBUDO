from django.shortcuts import render

# Create your views here.
def ver_sanciones_estudiante(request):
    return render(request, 'sanciones_estudiante/ver_sanciones_estudiante.html', {})