from django.urls import path
from authentication.views.profile import user_profile
from .views.update_profile import update_user
from authentication.views.change_password import change_password_api
from .views.register import register_user, register_user2

urlpatterns = [
    path('<int:user_id>/<str:active_tab>/', user_profile, name='user_profile'),
    path('<int:user_id>/', user_profile, name='user_profile'),

    path('registrar_2/', register_user2, name="register_form"),

    path('', register_user.as_view(), name="register_user"),

    path('<int:user_id>/update', update_user, name='update_user'),
    path('api/change_password/', change_password_api, name='change_password_api'),
    # path('<int:user_id>', delete_user, name='delete_user'),
]
