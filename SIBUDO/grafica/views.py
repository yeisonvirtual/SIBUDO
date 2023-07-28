from django.shortcuts import render
from django.contrib.auth.models import Group

def grafica(request):
    rol_aviable = ['Estudiante', 'Bibliotecario', 'Invitado']

    # Crear una lista para almacenar las tuplas de rol y contador
    series = []
    labels = []
    for rol in rol_aviable:
        num_users_in_group = contar_grupo(rol)
        series.append((num_users_in_group))
        labels.append((rol))

    context = {
        'Pie_Chart_series': series,
        'Pie_Chart_labels': labels,
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




