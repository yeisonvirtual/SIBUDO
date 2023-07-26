from django.contrib import admin
from django.urls import path
from authentication.views.profile import user_profile
from authentication.views.change_password import change_password_api
from .views.register import register_user
from .views.views import user_table
from . import views

urlpatterns = [
    path('', views.gestion_usuarios, name="Gestion_usuarios"),
    path('editar_usuario/', views.editar_usuario, name="Editar_usuario"),

    path('<int:user_id>/<str:active_tab>/', user_profile, name='user_profile'),
    path('<int:user_id>/', user_profile, name='user_profile'),

    path('', register_user.as_view(), name="register_user"),

    path('api/change_password/', change_password_api, name='change_password_api'),
    path('tabla_de_usuarios', user_table, name='user_table'),
]
