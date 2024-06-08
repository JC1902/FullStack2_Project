from django.views.generic import ListView  , DetailView
from .models import Juego
from django.db.models import Q

# Create your views here.

class VistaListaJuegos ( ListView ):
    model = Juego
    context_object_name = 'lista_juegos'
    template_name =  'juegos/lista_juegos.html'

class VistaDetalleJuego ( DetailView ):
    model = Juego
    context_object_name = 'juego'
    template_name = 'juegos/detalle_juego.html' 

class VistaResultadosBusqueda ( ListView ):
    model = Juego
    context_object_name = 'lista_juegos'
    template_name =  'juegos/resultados_busqueda.html'
    
    def get_queryset(self):
        consulta = self.request.GET.get('q')
        return Juego.objects.filter( Q( titulo__icontains = consulta) | Q( precio__icontains = consulta ) )
    
    
