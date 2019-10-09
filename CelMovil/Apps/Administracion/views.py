from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .forms import AccesoriosForm, ClientesForm
from .models import Accesorios, Clientes
from django.urls import reverse_lazy
# Create your views here.
class HomeView(TemplateView):
	template_name='Administracion/home.html'

# Vistas para el CRUD de Accesorios
class ListarAccesorio(ListView):
	template_name = 'Administracion/accesorios_list_form.html'
	model = Accesorios
	
	def get_queryset(self):
		return Accesorios.objects.all()

class CrearAccesorio(CreateView):
	template_name='Administracion/accesorios_create_form.html'
	form_class = AccesoriosForm
	success_url = reverse_lazy('Administracion:ListarAccesorio')

class ActualizarAccesorio(UpdateView):
    model = Accesorios
    form_class = AccesoriosForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('Administracion:ListarAccesorio')

class EliminarAccesorio(DeleteView):
    template_name='Administracion/accesorios_confirm_delete_form.html'	
    model = Accesorios
    form_class = AccesoriosForm    
    success_url = reverse_lazy('Administracion:ListarAccesorio')
#Fin de Vistas de CRUD Accesorios

# Vistas para el CRUD de Clientes
class ListarCliente(ListView):
	template_name = 'Administracion/clientes_list_form.html'
	model = Clientes
	
	def get_queryset(self):
		return Clientes.objects.all()

#class CrearCliente(CreateView):
#	template_name='Administracion/clientes_create_form.html'
#	form_class = AccesoriosForm
#	success_url = reverse_lazy('Administracion:ListarAccesorio')

#class ActualizarCliente(UpdateView):
#    model = Accesorios
#    form_class = AccesoriosForm
#    template_name_suffix = '_update_form'
#    success_url = reverse_lazy('Administracion:ListarAccesorio')

#class EliminarCliente(DeleteView):
#    template_name='Administracion/clientes_confirm_delete_form.html'	
#    model = Accesorios
#    form_class = AccesoriosForm    
#    success_url = reverse_lazy('Administracion:ListarAccesorio')
#Fin de Vistas de CRUD Clientes