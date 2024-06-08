from django.urls import path

from .views import VistaListaJuegos , VistaDetalleJuego , VistaResultadosBusqueda , VistaDejarResenha

urlpatterns = [
    path('', VistaListaJuegos.as_view(), name='lista_juegos'),
    path ( '<uuid:pk>/', VistaDetalleJuego.as_view() , name='detalle_juego' ),
    path ( 'buscar/' , VistaResultadosBusqueda.as_view() , name = 'resultados_busqueda' ),
    path('<uuid:pk>/dejar_resenha/' , VistaDejarResenha.as_view() , name='dejar_resenha' ) 
] 