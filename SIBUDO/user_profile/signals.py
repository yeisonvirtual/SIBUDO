# from django.db.models.signals import post_migrate
# from django.dispatch import receiver
# from django.contrib.auth.models import Group

# @receiver(post_migrate)
# def create_default_groups(sender, **kwargs):
#     if sender.name == 'auth':
#         groups = [
#             {'name': 'Invitados'},
#             {'name': 'Directores'},
#             {'name': 'Estudiantes'},
#             {'name': 'Bibliotecarios'},
#         ]
#         for group_data in groups:
#             group, created = Group.objects.get_or_create(name=group_data['name'])
#             if created:
#                 print(f"Grupo '{group_data['name']}' creado exitosamente.")
#             else:
#                 print(f"El grupo '{group_data['name']}' ya existe.")
