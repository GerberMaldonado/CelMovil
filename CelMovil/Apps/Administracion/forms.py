from django import forms
from .models import Accesorios, Clientes, Celulares

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