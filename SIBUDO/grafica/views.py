from django.shortcuts import render
from django.contrib.auth.models import Group
from gestion_recursos.models import cantidad_libro, cantidad_trabajo
from gestion_prestamos.models import Recurso_Disponible
from django.db.models import Sum

def grafica(request):
    rol_aviable = ['Estudiante', 'Bibliotecario', 'Invitado']

    # Crear una lista para almacenar las tuplas de rol y contador
    series = []
    labels = []
    for rol in rol_aviable:
        num_users_in_group = contar_grupo(rol)
        series.append((num_users_in_group))
        labels.append((rol))

    n_libros = obtener_cantidad_total_libros()
    n_trabajos = obtener_cantidad_total_trabajos()
    n_disponibles = obtener_cantidad_total_recursos_disponibles()
    n_prestados = (n_libros + n_trabajos) - n_disponibles

    context = {
        'Pie_Chart_series': series,
        'Pie_Chart_labels': labels,
        'n_libros': n_libros,
        'n_trabajos': n_trabajos,
        'n_disponible': n_disponibles,
        'n_prestados': n_prestados,
    }

    return render(request, 'grafica/grafica.html', context)

def contar_grupo(group_name):

    try:
        # Obtenemos el objeto Group correspondiente al nombre del grupo especificado
        group = Group.objects.get(name=group_name)
        # Obtenemos el número de usuarios que pertenecen a ese grupo
        num_users_in_group = group.user_set.count()
    except Group.DoesNotExist:
        # Manejo de excepción si el grupo no existe
        num_users_in_group = 0

    return num_users_in_group


def obtener_cantidad_total_libros():
    try:
        cantidad_total = cantidad_libro.objects.aggregate(total_libros=Sum('cantidad'))['total_libros']
        if cantidad_total is None:
            cantidad_total = 0
    except cantidad_libro.DoesNotExist:
        cantidad_total = 0

    return cantidad_total

def obtener_cantidad_total_trabajos():
    try:
        cantidad_total = cantidad_trabajo.objects.aggregate(total_trabajos=Sum('cantidad'))['total_trabajos']
        if cantidad_total is None:
            cantidad_total = 0
    except cantidad_trabajo.DoesNotExist:
        cantidad_total = 0

    return cantidad_total

def obtener_cantidad_total_recursos_disponibles():
    try:
        cantidad_total = Recurso_Disponible.objects.aggregate(total_recursos=Sum('n_disponibles'))['total_recursos']
        if cantidad_total is None:
            cantidad_total = 0
    except Recurso_Disponible.DoesNotExist:
        cantidad_total = 0

    return cantidad_total

