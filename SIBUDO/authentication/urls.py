from django.contrib import admin
from django.urls import path

from .views.login import sign_off, sing_in
from .views.views import not_fount

urlpatterns = [
    
    path('logout', sign_off, name="logout"),
    path('sing_in', sing_in, name="sing_in"),
    path('error_404/', not_fount, name="not_fount"),
]
