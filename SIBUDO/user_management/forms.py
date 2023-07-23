from django import forms
from django.forms import widgets
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class register_user_form(forms.Form):
#     nombre = forms.CharField(max_length=100)
#     apellido = forms.CharField(max_length=100)
#     correo = forms.EmailField()
#     contraseña = forms.CharField(widget=forms.PasswordInput)
#     confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)
#     fecha_de_cumpleaños = forms.DateField(widget=widgets.DateInput(attrs={'type': 'date'}))
#     Genero = forms.ChoiceField(choices=[('H', 'Hombre'), ('F', 'Mujer'), ('N', 'Prefiero no definirlo')])

#     def clean(self):
#         cleaned_data = super().clean()
#         contraseña = cleaned_data.get('contraseña')
#         confirmar_contraseña = cleaned_data.get('confirmar_contraseña')

#         if contraseña and confirmar_contraseña and contraseña != confirmar_contraseña:
#             raise forms.ValidationError("Las contraseñas no coinciden")

class register_user_form(UserCreationForm):
    nombre = forms.CharField(max_length=30, required=True)
    apellido = forms.CharField(max_length=30, required=True)
    correo = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'nombre', 'apellido', 'correo', 'password1', 'password2']