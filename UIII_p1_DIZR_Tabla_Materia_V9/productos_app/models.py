from django.db import models

# Create your models here.
class Productos(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    costo=models.CharField(max_length=100)
    descripcion= models.CharField(max_length=10)
    instrucciones=models.CharField(max_length=100)
    ingredientes=models.CharField(max_length=100)
    caducidad = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre
    