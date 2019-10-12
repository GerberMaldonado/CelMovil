from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .forms import AccesoriosForm, ClientesForm, CelularesForm, ChipsForm
from .models import Accesorios, Clientes, Celulares, Chips
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

class CrearCliente(CreateView):
	template_name='Administracion/clientes_create_form.html'
	form_class = ClientesForm
	success_url = reverse_lazy('Administracion:ListarCliente')

class ActualizarCliente(UpdateView):
    model = Clientes
    form_class = ClientesForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('Administracion:ListarCliente')

class EliminarCliente(DeleteView):
    template_name='Administracion/clientes_confirm_delete_form.html'	
    model = Clientes
    form_class = ClientesForm    
    success_url = reverse_lazy('Administracion:ListarCliente')
#Fin de Vistas de CRUD Clientes

# Vistas para el CRUD de Celulares
class ListarCelulares(ListView):
	template_name = 'Administracion/celulares_list_form.html'
	model = Celulares
	
	def get_queryset(self):
		return Celulares.objects.all()

class CrearCelulares(CreateView):
	template_name='Administracion/celulares_create_form.html'
	form_class = CelularesForm
	success_url = reverse_lazy('Administracion:ListarCelulares')

class ActualizarCelulares(UpdateView):
    model = Celulares
    form_class = CelularesForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('Administracion:ListarCelulares')

class EliminarCelulares(DeleteView):
    template_name='Administracion/celulares_confirm_delete_form.html'	
    model = Celulares
    form_class = CelularesForm    
    success_url = reverse_lazy('Administracion:ListarCelulares')
#Fin de Vistas de CRUD Celulares

# Vistas para el CRUD de Chips
class ListarChips(ListView):
	template_name = 'Administracion/chips_list_form.html'
	model = Chips
	
	def get_queryset(self):
		return Chips.objects.all()

class CrearChips(CreateView):
	template_name='Administracion/chips_create_form.html'
	form_class = ChipsForm
	success_url = reverse_lazy('Administracion:ListarChips')

class ActualizarChips(UpdateView):
    model = Chips
    form_class = ChipsForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('Administracion:ListarChips')

class EliminarChips(DeleteView):
    template_name='Administracion/chips_confirm_delete_form.html'	
    model = Chips
    form_class = ChipsForm    
    success_url = reverse_lazy('Administracion:ListarChips')
#Fin de Vistas de CRUD Chips