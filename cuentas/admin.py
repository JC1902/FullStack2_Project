from django.contrib import admin
from .models import Usuario

# Register your models here.
class UsuarioAdmin( admin.ModelAdmin ):
    pass
    #list_display = ( '' )

admin.site.register( Usuario, UsuarioAdmin )