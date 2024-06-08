from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import FormularioCreacionUsuario
from .models import Usuario

# Create your views here.
class VistaPaginaRegistro( CreateView ):
    form_class = FormularioCreacionUsuario
    model = Usuario
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'