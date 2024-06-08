from django.contrib import admin
from .models import Juego , Resenha
# Register your models here.


class ResenhaEnLinea ( admin.TabularInline ):
    model = Resenha

class JuegoAdmin ( admin.ModelAdmin ):
    inlines = (

      ResenhaEnLinea,
    )

    list_display = ( 'titulo' , 'sinopsis' , 'precio' )
   


# Register your models here.
admin.site.register( Juego , JuegoAdmin )

