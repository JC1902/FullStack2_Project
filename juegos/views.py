from django.views.generic import ListView  , DetailView , CreateView
from .models import Juego , Resenha
from .forms import FormularioNuevaResenha
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import get_object_or_404

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
    

class VistaDejarResenha( CreateView):
    model = Resenha
    form_class = FormularioNuevaResenha
    template_name = 'juegos/dejar_resenha.html'
   
    def form_valid(self, form):
        juego = get_object_or_404(Juego, pk=self.kwargs['pk'])
        form.instance.juego = juego
        form.instance.autor = self.request.user  # Asignar el usuario autenticado al autor
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.juego.get_absolute_url()

 

    
    
