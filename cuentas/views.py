from django.views.generic import CreateView
from .models import Usuario

# Create your views here.
class VistaPaginaRegistro( CreateView ):
    model = Usuario
    template_name = 'registration/signup.html'