from django import forms
from .models import Accesorios, Clientes, Celulares, Chips, Reparaciones, Repuestos

class AccesoriosForm(forms.ModelForm):
	class Meta:
		model = Accesorios
		fields = '__all__'

class ClientesForm(forms.ModelForm):
	class Meta:
		model = Clientes
		fields = '__all__'

class CelularesForm(forms.ModelForm):
	class Meta:
		model = Celulares
		fields = '__all__'

class ChipsForm(forms.ModelForm):
	class Meta:
		model = Chips
		fields = '__all__'

class ReparacionesForm(forms.ModelForm):
	class Meta:
		model = Reparaciones
		fields = '__all__'
		widgets = {
		'descripcionfalla': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
		'fechasalida': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
		'costo': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
		'clientes': forms.Select(attrs={'class': 'form-control fill'}),
		}
		
class RepuestosForm(forms.ModelForm):
	class Meta:
		model = Repuestos
		fields = '__all__'
		widgets = {
		'codigo': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
		'nombre': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
		'marca': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
		'modelo': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
		'cantidad': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
		'preciomayor': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
		'preciounidad': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
		'reparaciones': forms.Select(attrs={'class': 'forms-control fill'}),
		}