from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView  , DetailView , CreateView, CreateView
from .models import Juego, Categoria, RelacionCategoria
from .forms import FormularioCategoria, FormularioJuego , Resenha
from .forms import FormularioNuevaResenha
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin

# Create your views here.

class VistaListaJuegos ( ListView ):
    model = Juego
    context_object_name = 'lista_juegos'
    template_name =  'juegos/lista_juegos.html'

    def get_queryset(self):
        categoria_id = self.kwargs.get('categoria_id')
        if categoria_id:
            categoria = get_object_or_404(Categoria, id=categoria_id)
            categoria_relacionada = categoria.categorias_referenciadas.all()
            return Juego.objects.filter(categorias__in=[categoria, *categoria_relacionada]).distinct()
        return Juego.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

class VistaDetalleJuego ( LoginRequiredMixin , DetailView ):
    model = Juego
    context_object_name = 'juego'
    template_name = 'juegos/detalle_juego.html' 
    login_url = "account_login"

class VistaResultadosBusqueda ( ListView ):
    model = Juego
    context_object_name = 'lista_juegos'
    template_name =  'juegos/resultados_busqueda.html'
    
    def get_queryset(self):
        consulta = self.request.GET.get('q')
        return Juego.objects.filter( Q( titulo__icontains = consulta) | Q( precio__icontains = consulta ) )
    

class VistaDejarResenha( LoginRequiredMixin , CreateView):
    model = Resenha
    form_class = FormularioNuevaResenha
    template_name = 'juegos/dejar_resenha.html'
    login_url = "account_login"
   
    def form_valid(self, form):
        juego = get_object_or_404(Juego, pk=self.kwargs['pk'])
        form.instance.juego = juego
        form.instance.autor = self.request.user  #
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.juego.get_absolute_url()

 

    
    
class VistaJuegoNuevo( CreateView ):
    model = Juego
    form_class = FormularioJuego
    template_name = 'juegos/juego_nuevo.html'

    def form_valid(self, form):
        juego = form.save(commit=False)
        # Obtener la categoría principal del formulario
        categoria_principal = form.cleaned_data['categoria_principal']
        
        # Verificar si la categoría principal existe
        if not Categoria.objects.filter(nombre=categoria_principal).exists():
            # Si no existe, crearla
            nueva_categoria_principal = Categoria.objects.create(nombre=categoria_principal)
            juego.categorias.add(nueva_categoria_principal)
        else:
            # Si existe, obtenerla de la base de datos
            nueva_categoria_principal = Categoria.objects.get(nombre=categoria_principal)
            juego.categorias.add(nueva_categoria_principal)
        
        # Guardar las categorías relacionadas
        categorias_relacionadas = form.cleaned_data['categorias_relacionadas']
        juego.categorias.add(*categorias_relacionadas)
        
        juego.save()
        
        return redirect(juego.get_absolute_url())