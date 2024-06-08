from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import FormularioCreacionUsuario, FormularioModificacionUsuario
from .models import Usuario

# Register your models here.
class UsuarioAdmin( UserAdmin ):
    add_form = FormularioCreacionUsuario
    form = FormularioModificacionUsuario
    model = Usuario
    list_display = [
        'email',
        'username',
        'edad',
        'is_staff',
    ]

    fieldsets = UserAdmin.fieldsets + ( ( None, { 'fields': ( 'edad', ) } ), )
    add_fieldsets = UserAdmin.add_fieldsets + ( ( None, { 'fields': ( 'edad', ) } ), )

admin.site.register( Usuario, UsuarioAdmin )