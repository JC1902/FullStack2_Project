from django.views.generic import ListView  , DetailView
from .models import Juego
# Create your views here.

class VistaListaJuegos ( ListView ):
    model = Juego
    context_object_name = 'lista_juegos'
    template_name =  'juegos/lista_juegos.html'

class VistaDetalleJuego ( DetailView ):
    model = Juego
    context_object_name = 'juego'
    template_name = 'juegos/detalle_juego.html' 

