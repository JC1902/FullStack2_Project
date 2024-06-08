from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Usuario( AbstractUser ):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('registration/login') 
    edad = models.PositiveBigIntegerField ( null = True , blank = True )
