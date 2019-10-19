from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .forms import AccesoriosForm, ClientesForm, CelularesForm, ChipsForm, ReparacionesForm, RepuestosForm
from .models import Accesorios, Clientes, Celulares, Chips, Reparaciones, Repuestos
from django.urls import reverse_lazy
from django.shortcuts import redirect
# Create your views here.

# Redireccionamiento si no esta autenticado
class StaffRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))        
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class HomeView(StaffRequiredMixin, TemplateView):
	template_name='Administracion/home.html'

# Vistas para el CRUD de Accesorios
class ListarAccesorio(StaffRequiredMixin, ListView):
	template_name = 'Administracion/accesorios/accesorios_list_form.html'
	model = Accesorios
	
	def get_queryset(self):
		return Accesorios.objects.all()

class CrearAccesorio(StaffRequiredMixin, CreateView):
	template_name='Administracion/accesorios/accesorios_create_form.html'
	form_class = AccesoriosForm
	success_url = reverse_lazy('Administracion:ListarAccesorio')

class ActualizarAccesorio(StaffRequiredMixin, UpdateView):
    model = Accesorios
    form_class = AccesoriosForm
    template_name_suffix = '/accesorios_update_form'
    success_url = reverse_lazy('Administracion:ListarAccesorio')

class EliminarAccesorio(StaffRequiredMixin, DeleteView):
    template_name='Administracion/accesorios/accesorios_confirm_delete_form.html'	
    model = Accesorios
    form_class = AccesoriosForm    
    success_url = reverse_lazy('Administracion:ListarAccesorio')
#Fin de Vistas de CRUD Accesorios

# Vistas para el CRUD de Clientes
class ListarCliente(StaffRequiredMixin, ListView):
	template_name = 'Administracion/clientes/clientes_list_form.html'
	model = Clientes
	
	def get_queryset(self):
		return Clientes.objects.all()

class CrearCliente(StaffRequiredMixin, CreateView):
	template_name='Administracion/clientes/clientes_create_form.html'
	form_class = ClientesForm
	success_url = reverse_lazy('Administracion:ListarCliente')

class ActualizarCliente(StaffRequiredMixin, UpdateView):
    model = Clientes
    form_class = ClientesForm
    template_name_suffix = '/clientes_update_form'
    success_url = reverse_lazy('Administracion:ListarCliente')

class EliminarCliente(StaffRequiredMixin, DeleteView):
    template_name='Administracion/clientes/clientes_confirm_delete_form.html'	
    model = Clientes
    form_class = ClientesForm    
    success_url = reverse_lazy('Administracion:ListarCliente')
#Fin de Vistas de CRUD Clientes

# Vistas para el CRUD de Celulares
class ListarCelulares(StaffRequiredMixin, ListView):
	template_name = 'Administracion/celulares/celulares_list_form.html'
	model = Celulares
	
	def get_queryset(self):
		return Celulares.objects.all()

class CrearCelulares(StaffRequiredMixin, CreateView):
	template_name='Administracion/celulares/celulares_create_form.html'
	form_class = CelularesForm
	success_url = reverse_lazy('Administracion:ListarCelulares')

class ActualizarCelulares(StaffRequiredMixin, UpdateView):
    model = Celulares
    form_class = CelularesForm
    template_name_suffix = '/celulares_update_form'
    success_url = reverse_lazy('Administracion:ListarCelulares')

class EliminarCelulares(StaffRequiredMixin, DeleteView):
    template_name='Administracion/celulares/celulares_confirm_delete_form.html'	
    model = Celulares
    form_class = CelularesForm    
    success_url = reverse_lazy('Administracion:ListarCelulares')
#Fin de Vistas de CRUD Celulares

# Vistas para el CRUD de Chips
class ListarChips(StaffRequiredMixin, ListView):
	template_name = 'Administracion/chips/chips_list_form.html'
	model = Chips
	
	def get_queryset(self):
		return Chips.objects.all()

class CrearChips(StaffRequiredMixin, CreateView):
	template_name='Administracion/chips/chips_create_form.html'
	form_class = ChipsForm
	success_url = reverse_lazy('Administracion:ListarChips')

class ActualizarChips(StaffRequiredMixin, UpdateView):
    model = Chips
    form_class = ChipsForm
    template_name_suffix = '/chips_update_form'
    success_url = reverse_lazy('Administracion:ListarChips')

class EliminarChips(StaffRequiredMixin, DeleteView):
    template_name='Administracion/chips/chips_confirm_delete_form.html'	
    model = Chips
    form_class = ChipsForm    
    success_url = reverse_lazy('Administracion:ListarChips')
#Fin de Vistas de CRUD Chips

# Vistas para el CRUD de Reparaciones
class ListarReparaciones(StaffRequiredMixin, ListView):
    template_name = 'Administracion/reparaciones/reparaciones_list_form.html'
    model = Reparaciones
    
    def get_queryset(self):
        return Reparaciones.objects.all()

class CrearReparaciones(StaffRequiredMixin, CreateView):
    template_name='Administracion/reparaciones/reparaciones_create_form.html'
    form_class = ReparacionesForm
    success_url = reverse_lazy('Administracion:ListarReparaciones')

class ActualizarReparaciones(StaffRequiredMixin, UpdateView):
    model = Reparaciones
    form_class = ReparacionesForm
    template_name_suffix = '/reparaciones_update_form'
    success_url = reverse_lazy('Administracion:ListarReparaciones')

class EliminarReparaciones(StaffRequiredMixin, DeleteView):
    template_name='Administracion/reparaciones/reparaciones_confirm_delete_form.html' 
    model = Reparaciones
    form_class = ReparacionesForm    
    success_url = reverse_lazy('Administracion:ListarReparaciones')
#Fin de Vistas de CRUD Reparaciones

# Vistas para el CRUD de Repuestos
class ListarRepuestos(StaffRequiredMixin, ListView):
    template_name = 'Administracion/repuestos/repuestos_list_form.html'
    model = Repuestos
    
    def get_queryset(self):
        return Repuestos.objects.all()

class CrearRepuestos(StaffRequiredMixin, CreateView):
    template_name='Administracion/repuestos/repuestos_create_form.html'
    form_class = RepuestosForm
    success_url = reverse_lazy('Administracion:ListarRepuestos')

class ActualizarRepuestos(StaffRequiredMixin, UpdateView):
    model = Repuestos
    form_class = RepuestosForm
    template_name_suffix = '/repuestos_update_form'
    success_url = reverse_lazy('Administracion:ListarRepuestos')

class EliminarRepuestos(StaffRequiredMixin, DeleteView):
    template_name='Administracion/repuestos/repuestos_confirm_delete_form.html' 
    model = Repuestos
    form_class = RepuestosForm    
    success_url = reverse_lazy('Administracion:ListarRepuestos')
#Fin de Vistas de CRUD Repuestos