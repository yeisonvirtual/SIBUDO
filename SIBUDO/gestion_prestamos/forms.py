from django import forms

class DatePicker(forms.Form):
    new_date = forms.DateField(label='Fecha Devolucion', required=True, widget=forms.DateInput(
        attrs={
            'type':'date',
            'class': 'form-control'
        }
    ))