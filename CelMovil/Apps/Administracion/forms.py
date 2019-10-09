from django import forms
from .models import Accesorios, Clientes

class AccesoriosForm(forms.ModelForm):
	class Meta:
		model = Accesorios
		fields = '__all__'

class ClientesForm(forms.ModelForm):
	class Meta:
		model = Clientes
		fields = '__all__'		