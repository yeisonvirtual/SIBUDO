from django.shortcuts import render

# Create your views here.
def ver_sanciones(request):
    return render(request, 'sanciones_estudiante/ver_sanciones.html', {'param':'Este es el param'})