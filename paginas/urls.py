from django.urls import path
from .views import VistaPaginaInicio, VistaPaginaNosotros

urlpatterns = [
    path('', VistaPaginaInicio.as_view(), name='inicio'),
    path('sobre_nosotros/', VistaPaginaNosotros.as_view(), name='sobre_nosotros'),
]