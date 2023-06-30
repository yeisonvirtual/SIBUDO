from django import forms

class Formulario_usuario(forms.Form):
    cedula = forms.CharField(label="Cedula", required=True)
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    usuario = forms.CharField(label="Usuario", required=True)
    rol = forms.CharField(label="Rol", required=True)
    estado = forms.CharField(label="Estado", required=True)