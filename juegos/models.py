from django.db import models
import uuid 


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
    #portada = models.ImageField( upload_to='portadas/' , blank=True)


    def __str__(self) -> str:
        return self.titulo

  
    
 


    