from django import forms
from datetime import datetime

class formulario_libro(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    autor = forms.CharField(label="Autor", required=True)
    edicion = forms.IntegerField(label="Edición", required=True)
    anio = forms.IntegerField(label="Año", required=True)
    isbn = forms.CharField(label="ISBN", required=True)
    cantidad = forms.IntegerField(label="Cantidad", required=True)


class formulario_trabajo(forms.Form):
    titulo = forms.CharField(label="Título", required=True)
    autor = forms.CharField(label="Autor", required=True)
    palabras_clave = forms.CharField(label="Palabras", required=True)
    fecha = forms.DateField(label="Fecha", required=True, widget=forms.DateInput(
        attrs={
            'type':'date',
            'class': 'form-control'
        }
    ))
    cantidad = forms.IntegerField(label="Cantidad", required=True)