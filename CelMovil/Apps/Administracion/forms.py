from django import forms

from .models import Accesorios

class AccesoriosForm(forms.ModelForm):
	class Meta:
		model: Accesorios
		fields: '__all__'