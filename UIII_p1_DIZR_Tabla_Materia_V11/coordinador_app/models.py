from django.db import models

# Create your models here.
class Coordinador(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    zona=models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    direccion=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    sueldo = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre
    