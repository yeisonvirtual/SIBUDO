from django import forms

class DatePicker(forms.Form):
    new_date = forms.DateField(label='Fecha Devolucion', required=True, widget=forms.DateInput(
        attrs={
            'type':'date',
            'class': 'form-control'
        }
    ))

class Penalty_DatePicker(forms.Form):
    penalty_date = forms.DateField(label='Fecha final de sancion', required=True, widget=forms.DateInput(
        attrs={
            'type':'date',
            'class': 'form-control'
        }
    ))

class CI_Form(forms.Form):
    ci = forms.IntegerField(label='Cédula de Identidad', required=True)

class Selector_Recurso_Form(forms.Form):
    my_choises = (
        ('1', 'Libros'),
        ('2', 'Trabajos de Grado'),
    )
    selector = forms.ChoiceField(label='Tipo de Recurso', required=False, choices=my_choises, widget=forms.Select(
        attrs={
            'placeholder':'Selecciona una opción',
            'class':'form-select',
        }
    ))