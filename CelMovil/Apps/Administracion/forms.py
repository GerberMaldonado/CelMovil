from django import forms
from .models import Accesorio, Empleado, Cliente, Celular, Chip, Reparacion, Repuesto, Venta, DetalleVenta

class AccesoriosForm(forms.ModelForm):
	class Meta:
		model = Accesorio
		fields = '__all__'
		widgets = {
		'codigo': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'nombre': forms.TextInput(attrs={'class': 'form-control', 'type': 'text','required': '' }),
		'marca': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'cantidad': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'required': ''}),		
		}		

class EmpleadosForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = '__all__'
		widgets = {
		'nombre': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'apellido': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'required': ''}),
		'dpi': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'required': ''}),
		'telefono': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'required': ''}),				
		'rol': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		}				

class ClientesForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = '__all__'
		widgets = {
		'nombre': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'apellido': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'telefono': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'required': ''}),				
		'dpi': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'required': ''}),
		'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'required': ''}),		
		'direccion': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		}			

class CelularesForm(forms.ModelForm):
	class Meta:
		model = Celular
		fields = '__all__'
		widgets = {
		'codigo': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'marca': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'serieimei': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),				
		'preciomayor': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'required': ''}),
		'preciounidad': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'required': ''}),				
		}		

class ChipsForm(forms.ModelForm):
	class Meta:
		model = Chip
		fields = '__all__'
		widgets = {
		'codigo': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'operador': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'serie': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),						
		}		

class ReparacionesForm(forms.ModelForm):
	class Meta:
		model = Reparacion
		fields = '__all__'
		widgets = {
		'descripcionfalla': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'fechasalida': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'required': ''}),
		'costo': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'required': ''}),
		'clientes': forms.Select(attrs={'class': 'form-control fill', 'required': ''}),
		}
		
class RepuestosForm(forms.ModelForm):
	class Meta:
		model = Repuesto
		fields = '__all__'
		widgets = {
		'codigo': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'nombre': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'marca': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'modelo': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': ''}),
		'cantidad': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'required': ''}),
		'preciomayor': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'required': ''}),
		'preciounidad': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'required': ''}),
		'reparaciones': forms.Select(attrs={'class': 'form-control fill', 'required': ''}),
		}

class VentasForm(forms.ModelForm):
	class Meta:
		model = Venta
		fields = '__all__'
		widgets = {
        'clientes': forms.Select(attrs={'class': 'form-control fill', 'required': ''}),
		'empleados': forms.Select(attrs={'class': 'form-control fill', 'required': ''}),
		}

class DetalleVentasForm(forms.ModelForm):
	class Meta:
		model = DetalleVenta
		fields = '__all__'
		widgets = {
		'accesorios': forms.Select(attrs={'class': 'form-control fill', 'required': ''}),
		'celulares': forms.Select(attrs={'class': 'form-control fill', 'required': ''}),        		
		'chips': forms.Select(attrs={'class': 'form-control fill', 'required': ''}),
		'reparaciones': forms.Select(attrs={'class': 'form-control fill', 'required': ''}),		
		'ventas': forms.Select(attrs={'class': 'form-control fill', 'required': ''}),				
		}