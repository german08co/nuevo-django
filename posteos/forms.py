
from django import forms
from .models import Posteos

class formulario_posteos(forms.ModelForm):
    class Meta:
        model = Posteos
        fields = ['titulo_posteo', 'redaccion_posteo']



