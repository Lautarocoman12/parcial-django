from django import forms

class BuscarForm(forms.Form):
    q = forms.CharField(label='Palabra clave')
