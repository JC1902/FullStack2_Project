from django.db import models
from django.urls  import reverse
import uuid 
from django.contrib.auth import get_user_model

# Create your models here.
class Categoria( models.Model ):
    nombre = models.CharField( max_length = 100, unique = True )

    def __str__( self ):
        return self.nombre
    
    def get_absolute_url( self ):
        return reverse( "lista_juegos", args=[ str( self.id ) ] ) 

class RelacionCategoria(models.Model):
    categoria_principal = models.ForeignKey(
        Categoria, 
        related_name='categorias_relacionadas', 
        on_delete=models.CASCADE
        )
    categoria_relacionada = models.ForeignKey(
        Categoria, 
        related_name='relaciones_categorias', 
        on_delete=models.CASCADE
        )

    def __str__(self):
        return f'{self.categoria_principal} - {self.categoria_relacionada}'

class Juego( models.Model ):
    id = models.UUIDField (
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    titulo = models.CharField ( max_length=200 )
    sinopsis = models.CharField ( max_length=250 )
    precio = models.DecimalField ( max_digits=7 , decimal_places=2 )
    categoria = models.ManyToManyField( Categoria, related_name='juegos', blank=True )
    portada = models.ImageField( upload_to='portadas/' , blank=True)


    def __str__(self) -> str:
        return self.titulo
    

    def get_absolute_url(self):
        return reverse("detalle_juego", args=[ str(self.id) ])


class Resenha ( models.Model ):
    juego = models.ForeignKey (
        Juego,
        on_delete =  models.CASCADE,
        related_name = 'resenhas',
    )

    resenha = models.CharField( max_length = 255 )

    autor = models.ForeignKey (
        get_user_model(),
        on_delete =  models.CASCADE,

    )

    def __str__ ( self ):
        return self.resenha
  
    
 


    
