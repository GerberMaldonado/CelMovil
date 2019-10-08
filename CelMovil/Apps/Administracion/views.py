from django.views.generic import TemplateView, CreateView, ListView
from .forms import AccesoriosForm
from .models import Accesorios
from django.urls import reverse_lazy
# Create your views here.
class HomeView(TemplateView):
	template_name='Administracion/home.html'

class ListarClienteView(ListView):
	template_name = 'Administracion/listaraccesorios.html'
	model = Accesorios
	
	def get_queryset(self):
		return Accesorios.objects.all()

class CrearAccesorio(CreateView):
	template_name='Administracion/crearaccesorios.html'
	form_class = AccesoriosForm
	success_url = reverse_lazy('Administracion:Home')



