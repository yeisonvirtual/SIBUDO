from django import forms

class formulario_libro(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    autor = forms.CharField(label="Autor", required=True)
    edicion = forms.IntegerField(label="Edicion", required=True)
    anio = forms.IntegerField(label="Edicion", required=True)
    isbn = forms.CharField(label="ISBN", required=True)