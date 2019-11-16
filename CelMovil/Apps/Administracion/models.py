from django.db import models

# Create your models here.

class Accesorio(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    cantidad = models.FloatField()
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    dpi = models.CharField(max_length=30)
    telefono = models.IntegerField()
    rol = models.CharField(max_length=50)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)
    
class Celular(models.Model):
    codigo = models.CharField(max_length=50)
    marca = models.CharField(max_length=25)
    serieimei = models.CharField(max_length=50)
    preciomayor = models.FloatField()
    preciounidad = models.FloatField()
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.marca

class Chip(models.Model):
    codigo = models.CharField(max_length=50)
    operador = models.CharField(max_length=15)
    serie = models.CharField(max_length=8)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.codigo       

class Cliente(models.Model):
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

class Reparacion(models.Model):    
    descripcionfalla = models.CharField(max_length=200)    
    fechasalida = models.DateTimeField(null=True, blank=True)
    costo = models.FloatField()
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE)    
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcionfalla      
    
class Repuesto(models.Model):    
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    cantidad = models.FloatField()
    preciomayor = models.FloatField()
    preciounidad = models.FloatField() 
    reparaciones = models.ForeignKey(Reparacion, on_delete=models.CASCADE)    
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.marca, self.reparaciones)    

class Venta(models.Model):
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleados = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.clientes, self.empleados)           
    
class DetalleVenta(models.Model):
    accesorios = models.ForeignKey(Accesorio, on_delete=models.CASCADE, null=True, blank=True)
    celulares = models.ForeignKey(Celular, on_delete=models.CASCADE, null=True, blank=True)
    chips = models.ForeignKey(Chip, on_delete=models.CASCADE, null=True, blank=True)
    reparaciones = models.ForeignKey(Reparacion, on_delete=models.CASCADE, null=True, blank=True)
    ventas = models.ForeignKey(Venta, on_delete=models.CASCADE, null=True, blank=True)    
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)

      