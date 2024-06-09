from django import forms 
from .models import Juego, Categoria
from django_select2.forms import ModelSelect2MultipleWidget

class FormularioCategoria( forms.ModelForm ):
    class Meta:
        model = Categoria
        fields = [ 'nombre', ]

class FormularioJuego( forms.ModelForm ):
    categoria_principal = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        widget=ModelSelect2MultipleWidget(
            search_fields=['nombre__icontains'],
            attrs={'class': 'select2'}
        ),
        required=False,
        label='Seleccione la categoría principal'
    )

    categoria_relacionada = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=ModelSelect2MultipleWidget(
            search_fields=['nombre__icontains'],
            attrs={'class': 'select2'}
        ),
        required=False,
        label='Seleccione las categorías relacionadas'
    )

    class Meta:
        model = Juego
        fields = ['titulo', 'sinopsis', 'precio', 'categoria_principal', 'categoria_relacionada']
    

