from django.contrib import admin
from django.urls import path

from .views import register_user, sign_off, sing_in

urlpatterns = [
    path('', register_user.as_view(), name="authentication"),
    path('logout', sign_off, name="logout"),
    path('sing_in', sing_in, name="sing_in"),
]
