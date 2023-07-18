from django.apps import AppConfig
import user_profile.signals

class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'

    # def ready(self):
    #     import user_profile.signals  # Importa las señales aquí
            