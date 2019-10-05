from django.db import models

# Create your models here.

class Accesorios(models.Model):
    idAccesorios = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    marca = models.DateTimeField(auto_now_add=True)
    fechaingreso = models.DateTimeField(auto_now_add=True)
    cantidad = models.FloatField()

    