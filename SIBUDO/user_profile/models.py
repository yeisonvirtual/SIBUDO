from django.apps import AppConfig
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Group
# from django.db.models.signals import post_migrate
# from django.dispatch import receiver

class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'

    # def ready(self):
    #     import user_profile.signals  # Importa las señales aquí

# @receiver(post_migrate)
# def create_default_user(sender, **kwargs):
#     if sender.name == 'auth':
#         User = get_user_model()
#         username = 'director'  # Nombre de usuario a almacenar
#         user, created = User.objects.get_or_create(username='director')
#         if created:
#             user.set_password('asdF.1234')
#             user.save()
#             group = Group.objects.get(name='Director')
#             user.groups.add(group)
#             print(f"Usuario '{username}' creado exitosamente y asignado al grupo 'Director'.")
#         else:
#             print(f"El usuario '{username}' ya existe.")

