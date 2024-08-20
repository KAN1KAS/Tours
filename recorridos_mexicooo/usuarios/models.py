from django.db import models
from django.contrib.auth.models import User #MODELO creado django automatico

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=16)
    imagen = models.ImageField(null=True,upload_to="fotos")
    created= models.DateField(auto_now_add=True, verbose_name="fecha creación")

    class Meta:
        verbose_name= "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name= "Perfiles"
        verbose_name_plural = "Perfiles"
        
    def __str__(self):
        return self.user.username