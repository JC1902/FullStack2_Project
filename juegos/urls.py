from django.urls import path

from .views import VistaListaJuegos

urlpatterns = [
    path('', VistaListaJuegos.as_view(), name='lista_juegos'),
]