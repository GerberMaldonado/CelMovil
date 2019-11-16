from django.contrib import admin
from .models import Accesorio,Celular,Chip,Cliente,DetalleVenta,Reparacion,Repuesto,Empleado,Venta
# Register your models here.

admin.site.register(Accesorio)
admin.site.register(Celular)
admin.site.register(Chip)
admin.site.register(Cliente)
admin.site.register(DetalleVenta)
admin.site.register(Reparacion)
admin.site.register(Repuesto)
admin.site.register(Empleado)
admin.site.register(Venta)