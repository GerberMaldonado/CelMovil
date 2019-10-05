from django.db import models

# Create your models here.

class Accesorios(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    marca = models.DateTimeField(max_length=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    cantidad = models.FloatField()

    def __str__(self):
        return '%s %s' % (self.id_accesorios,self.nombre)

class Celulares(models.Model):
    codigo = models.FloatField()
    marca = models.CharField(max_length=25)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    serie_imei = models.DateTimeField(auto_now_add=True)
    precio_mayor = models.FloatField()
    precio_unidad = models.FloatField()

class Chips(models.Model):
	codigo = models.FloatField()
	operador = models.CharField(max_length=15)
	serie = models.CharField(max_length=8)
	fecha_ingreso = models.DateTimeField(auto_now_add=True)

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    DPI = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

class Detalle_Venta(models.Model):
    accesorios = models.ForeignKey(Accesorios, on_delete=models.CASCADE)

class Reparaciones(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion_falla = models.CharField(max_length=200)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(auto_now_add=True)
    costo = models.FloatField() 

class Repuestos(models.Model):
    reparaciones = models.ForeignKey(Reparaciones, on_delete=models.CASCADE)
    codigo = models.FloatField()
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    cantidad = models.FloatField()
    precio_mayor = models.FloatField()
    precio_unidad = models.FloatField()
    reparaciones_idReparaciones = models.CharField(max_length=10)

class Empleados(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	DPI = models.CharField(max_length=30)
	telefono = models.FloatField()
	rol = models.CharField(max_length=50)

class Usuario(models.Model):
    empleados = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)


class Ventas(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad_venta = models.FloatField()
    vendedor_id_vendedor = models.CharField(max_length=7)
    cliente_id_cliente = models.CharField(max_length=7)
    empleados_id_empleados = models.CharField(max_length=7)
    