from django.contrib import admin
from .models import Juego, Categoria , Resenha
# Register your models here.


class ResenhaEnLinea ( admin.TabularInline ):
    model = Resenha

class JuegoAdmin ( admin.ModelAdmin ):
    inlines = (

      ResenhaEnLinea,
    )

    list_display = ( 'titulo' , 'sinopsis' , 'precio' )
    
class CategoriaAdmin( admin.ModelAdmin ):
    list_display = ( 'nombre', )   


# Register your models here.
admin.site.register( Juego , JuegoAdmin )
admin.site.register( Categoria, CategoriaAdmin )

