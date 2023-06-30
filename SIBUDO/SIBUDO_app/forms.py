from django import forms
from django.forms import widgets

class register_user_form(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    correo = forms.EmailField()
    contraseña = forms.CharField(widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)
    fecha_de_cumpleaños =  forms.DateField(widget=widgets.DateInput(attrs={'type': 'date'}))
    Genero = forms.ChoiceField(choices=[('H', 'Hombre'), ('F', 'Mujer'), ('N', 'Prefiero no definirlo')])

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas con coninciden")
