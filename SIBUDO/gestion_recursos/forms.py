from django import forms

class formulario_libro(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    autor = forms.CharField(label="Autor", required=True)
    edicion = forms.IntegerField(label="Edición", required=True)
    anio = forms.IntegerField(label="Año", required=True)
    isbn = forms.CharField(label="ISBN", required=True)
    cantidad = forms.IntegerField(label="Cantidad", required=True)