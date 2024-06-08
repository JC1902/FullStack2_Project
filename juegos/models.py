from django.db import models
from django.urls  import reverse
import uuid 
from django.contrib.auth import get_user_model

 

# Create your models here.
class Juego( models.Model ):
    id = models.UUIDField (
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    titulo = models.CharField ( max_length=200 )
    sinopsis = models.CharField ( max_length=250 )
    precio = models.DecimalField ( max_digits=7 , decimal_places=2 )
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
  
    
 


    
