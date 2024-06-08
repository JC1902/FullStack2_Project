# forms.py
from django import forms
from .models import Resenha

class FormularioNuevaResenha(forms.ModelForm):
    class Meta:
        model = Resenha
        fields = ['resenha']
        widgets = {
            'resenha': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
