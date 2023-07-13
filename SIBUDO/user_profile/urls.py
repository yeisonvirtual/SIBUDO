from django.urls import path
from .views.crud_auth_user import user_profile, update_user
from .views.change_password import change_password_api

urlpatterns = [
    path('<int:user_id>/<str:active_tab>/', user_profile, name='user_profile'),
    path('<int:user_id>/', user_profile, name='user_profile'),


    path('<int:user_id>/update', update_user, name='update_user'),
    path('api/change_password/', change_password_api, name='change_password_api'),
    # path('<int:user_id>', delete_user, name='delete_user'),
]
