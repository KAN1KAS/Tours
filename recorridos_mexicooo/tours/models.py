from django.db import models

# Create your models here.
class Tours(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    km = models.CharField(max_length=20)
    tiempo_estimado = models.CharField(max_length=50)
    punto_inicio = models.CharField(max_length=100)
    costo = models.FloatField()
    ganancias = models.FloatField(null=True)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    imagen = models.ImageField(null=True,upload_to="fotos")
    created= models.DateField(auto_now_add=True, verbose_name="fecha creación")

    class Meta:
        verbose_name= "Tour"
        verbose_name_plural = "Tours"
        ordering = ["id"]

    def __str__(self):
        return self.nombre