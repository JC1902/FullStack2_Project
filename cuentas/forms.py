from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class FormularioCreacionUsuario( UserCreationForm ):
    class Meta( UserCreationForm ):
        model = Usuario
        fields = ( 'username', 'email', 'edad' )

class FormularioModificacionUsuario( UserChangeForm ):
    class Meta( UserChangeForm ):
        model = Usuario
        fields = ( 'username', 'email','edad' )
