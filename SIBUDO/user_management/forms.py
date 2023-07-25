from django import forms
from django.forms import widgets
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Persona
from django.core.validators import RegexValidator
from datetime import date

class User_form(UserCreationForm):
    correo = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'correo', 'password1', 'password2']

class Persona_Form(forms.ModelForm):

    cedula = forms.CharField(validators=[RegexValidator(r'^\d{7,8}$', 'La cédula debe contener entre 7 y 8 dígitos numéricos.')])
    nombre = forms.CharField(max_length=50, validators=[RegexValidator(r'^[A-Za-z]+$', 'El nombre debe contener solo letras.')])
    apellido = forms.CharField(max_length=50, validators=[RegexValidator(r'^[A-Za-z]+$', 'El apellido debe contener solo letras.')])
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    genero = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Femenina'), ('O', 'Prefiero no definirlo')])

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        edad_minima = 16  # Cambiar la edad mínima si es necesario
        today = date.today()
        edad = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

        if edad < edad_minima:
            raise forms.ValidationError(f"Debes tener al menos {edad_minima} años para registrarte.")
        
        return fecha_nacimiento

    class Meta:
        model = Persona
        fields = ['cedula', 'nombre', 'apellido', 'fecha_nacimiento', 'genero']

        
