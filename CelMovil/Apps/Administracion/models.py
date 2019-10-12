from django.db import models

# Create your models here.

class Accesorios(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    cantidad = models.FloatField()
    fechaingreso = models.DateTimeField()
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Empleados(models.Model):
    dpi = models.CharField(max_length=30)
    telefono = models.IntegerField()
    rol = models.CharField(max_length=50)

class Celulares(models.Model):
    codigo = models.CharField(max_length=50)
    marca = models.CharField(max_length=25)
    serieimei = models.CharField(max_length=50)
    preciomayor = models.FloatField()
    preciounidad = models.FloatField()
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.marca

class Chips(models.Model):
    codigo = models.CharField(max_length=50)
    operador = models.CharField(max_length=15)
    serie = models.CharField(max_length=8)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)     

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    dpi = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)     

    def __str__(self):
        return self.nombre   

class Reparaciones(models.Model):    
    descripcionfalla = models.CharField(max_length=200)    
    fechasalida = models.DateTimeField(null=True, blank=True)
    costo = models.FloatField()
    clientes = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)    
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)     
    
class Repuestos(models.Model):    
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    cantidad = models.FloatField()
    preciomayor = models.FloatField()
    preciounidad = models.FloatField() 
    reparaciones = models.ForeignKey(Reparaciones, on_delete=models.DO_NOTHING)    
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre    

class Ventas(models.Model):
    clientes = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)
    empleados = models.ForeignKey(Empleados, on_delete=models.DO_NOTHING)           
    
class DetalleVentas(models.Model):
    accesorios = models.ForeignKey(Accesorios, on_delete=models.DO_NOTHING, null=True, blank=True)
    celulares = models.ForeignKey(Celulares, on_delete=models.DO_NOTHING, null=True, blank=True)
    chips = models.ForeignKey(Chips, on_delete=models.DO_NOTHING, null=True, blank=True)
    reparaciones = models.ForeignKey(Reparaciones, on_delete=models.DO_NOTHING, null=True, blank=True)
    ventas = models.ForeignKey(Ventas, on_delete=models.DO_NOTHING, null=True, blank=True)    
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)  