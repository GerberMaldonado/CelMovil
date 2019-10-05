from django.views.generic import TemplateView
from .forms import AccesoriosForm
from django.views.generic import CreateView
# Create your views here.
class AdminView(TemplateView):
	template_name='Administracion/index.html'

class CrearAccesorio(CreateView):
	template_name = 'crear_accesorio.html'
	form_class = AccesoriosForm
	succes_url = 'admin'