from django.contrib import admin
from .models import Juego
# Register your models here.


class JuegoAdmin ( admin.ModelAdmin ):
   
    list_display = ( 'titulo' , 'sinopsis' , 'precio' )
   


# Register your models here.
admin.site.register( Juego , JuegoAdmin )

