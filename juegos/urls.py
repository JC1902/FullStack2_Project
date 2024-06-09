from django.urls import path

from .views import VistaListaJuegos , VistaDetalleJuego, VistaJuegoNuevo

urlpatterns = [
    path('', VistaListaJuegos.as_view(), name='lista_juegos'),
    path( '<uuid:pk>/', VistaDetalleJuego.as_view() , name='detalle_juego' ),
    path( 'nuevo/', VistaJuegoNuevo.as_view(), name='juego_nuevo' ),
    path('categoria/<int:categoria_id>/', VistaListaJuegos.as_view(), name='filtrar_juegos_por_categoria'),

]