from django.db import models

# Create your models here.

class Accesorios(models.Model):
    
    id_accesorios = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    marca = models.DateTimeField(max_length=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    cantidad = models.FloatField()

    def __str__(self):
        return '%s %s' % (self.id_accesorios,self.nombre)

class Celulares(models.Model):
    id_celulares = models.CharField(max_length=10)
    codigo = models.FloatField()
    marca = models.CharField(max_length=25)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    serie_imei = models.DateTimeField(auto_now_add=True)
    precio_mayor = models.FloatField()
    precio_unidad = models.FloatField()

class Chips(models.Model):
	id_chips = models.CharField(max_length=10)
	codigo = models.FloatField()
	operador = models.CharField(max_length=15)
	serie = models.CharField(max_length=8)
	fecha_ingreso = models.DateTimeField(auto_now_add=True)

class Cliente(models.Model):
    id_cliente = models.CharField(max_length=7)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    DPI = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

class Detalle_Venta(models.Model):
    id_detalle_venta = models.CharField(max_length=7)
    accesorios_id_accesorios = models.CharField(max_length=10)
    ventas_id_ventas = models.CharField(max_length=10)
    reparaciones_idreparaciones = models.CharField(max_length=10)
    chips_id_Chips = models.CharField(max_length=10)
    celulares_id_Celulares = models.CharField(max_length=20)

class Reparaciones(models.Model):
	id_reparaciones = models.CharField(max_length=7)
	descripcion_falla = models.CharField(max_length=200)
	fecha_ingreso = models.DateTimeField(auto_now_add=True)
	fecha_salida = models.DateTimeField(auto_now_add=True)
	costo = models.FloatField() 

class Repuestos(models.Model):
    id_repuestos = models.CharField(max_length=7)
    codigo = models.FloatField()
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    cantidad = models.FloatField()
    precio_mayor = models.FloatField()
    precio_unidad = models.FloatField()
    reparaciones_idReparaciones = models.CharField(max_length=10)

class Usuario(models.Model):
	id_Usuario = models.CharField(max_length=7)
	usuario = models.CharField(max_length=50)
	contraseña = models.CharField(max_length=50)
	empleados_id_empleados = models.CharField(max_length=7)

class Vendedor(models.Model):
	id_empleados = models.CharField(max_length=7)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	DPI = models.CharField(max_length=30)
	telefono = models.FloatField()
	rol = models.CharField(max_length=50)

class Ventas(models.Model):
	id_Ventas = models.CharField(max_length=7)
	fecha = models.DateTimeField(auto_now_add=True)
	cantidad_venta = models.FloatField()
	vendedor_id_vendedor = models.CharField(max_length=7)
	cliente_id_cliente = models.CharField(max_length=7)
	empleados_id_empleados = models.CharField(max_length=7) 