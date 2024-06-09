from django.contrib import admin
from .models import Juego, Categoria
# Register your models here.


class JuegoAdmin ( admin.ModelAdmin ):
    list_display = ( 'titulo' , 'sinopsis' , 'precio' )
    
class CategoriaAdmin( admin.ModelAdmin ):
    list_display = ( 'nombre', )   


# Register your models here.
admin.site.register( Juego , JuegoAdmin )
admin.site.register( Categoria, CategoriaAdmin )

