from django.views.generic import CreateView
from .forms import FormularioCreacionUsuario
from .models import Usuario

# Create your views here.
class VistaPaginaRegistro( CreateView ):
    form_class = FormularioCreacionUsuario
    model = Usuario
    template_name = 'registration/signup.html'