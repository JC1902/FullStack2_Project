from django.urls import path

from .views import VistaListaJuegos , VistaDetalleJuego

urlpatterns = [
    path('', VistaListaJuegos.as_view(), name='lista_juegos'),
    path ( '<uuid:pk>/', VistaDetalleJuego.as_view() , name='detalle_juego' ),
]