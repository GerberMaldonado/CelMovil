import io
from django.http import HttpResponseRedirect, HttpResponse
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, SimpleDocTemplate
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib import colors
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .forms import AccesoriosForm, EmpleadosForm, ClientesForm, CelularesForm, ChipsForm, ReparacionesForm, \
    RepuestosForm, VentasForm
from .models import Accesorios, Empleados, Clientes, Celulares, Chips, Reparaciones, Repuestos, Ventas
from django.urls import reverse_lazy
from django.shortcuts import redirect
# Create your views here.

class HomeView(TemplateView):
	template_name='Administracion/home.html'

# Vistas para el CRUD de Accesorios
class ListarAccesorio(ListView):
	template_name = 'Administracion/accesorios/accesorios_list_form.html'
	model = Accesorios
	
	def get_queryset(self):
		return Accesorios.objects.all()

class CrearAccesorio(CreateView):
	template_name='Administracion/accesorios/accesorios_create_form.html'
	form_class = AccesoriosForm
	success_url = reverse_lazy('Administracion:ListarAccesorio')

class ActualizarAccesorio(UpdateView):
    model = Accesorios
    form_class = AccesoriosForm
    template_name_suffix = '/accesorios_update_form'
    success_url = reverse_lazy('Administracion:ListarAccesorio')

class EliminarAccesorio(DeleteView):
    template_name='Administracion/accesorios/accesorios_confirm_delete_form.html'	
    model = Accesorios
    form_class = AccesoriosForm    
    success_url = reverse_lazy('Administracion:ListarAccesorio')
#Fin de Vistas de CRUD Accesorios

# Vistas para el CRUD de Empleados
class ListarEmpleados(ListView):
    template_name = 'Administracion/empleados/empleados_list_form.html'
    model = Empleados
    
    def get_queryset(self):
        return Empleados.objects.all()

class CrearEmpleados(CreateView):
    template_name='Administracion/empleados/empleados_create_form.html'
    form_class = EmpleadosForm
    success_url = reverse_lazy('Administracion:ListarEmpleados')

class ActualizarEmpleados(UpdateView):
    model = Empleados
    form_class = EmpleadosForm
    template_name_suffix = '/empleados_update_form'
    success_url = reverse_lazy('Administracion:ListarEmpleados')

class EliminarEmpleados(DeleteView):
    template_name='Administracion/empleados/empleados_confirm_delete_form.html'   
    model = Empleados
    form_class = EmpleadosForm    
    success_url = reverse_lazy('Administracion:ListarEmpleados')
#Fin de Vistas de CRUD Empleados

# Vistas para el CRUD de Clientes
class ListarCliente(ListView):
	template_name = 'Administracion/clientes/clientes_list_form.html'
	model = Clientes
	
	def get_queryset(self):
		return Clientes.objects.all()

class CrearCliente(CreateView):
	template_name='Administracion/clientes/clientes_create_form.html'
	form_class = ClientesForm
	success_url = reverse_lazy('Administracion:ListarCliente')

class ActualizarCliente(UpdateView):
    model = Clientes
    form_class = ClientesForm
    template_name_suffix = '/clientes_update_form'
    success_url = reverse_lazy('Administracion:ListarCliente')

class EliminarCliente(DeleteView):
    template_name='Administracion/clientes/clientes_confirm_delete_form.html'	
    model = Clientes
    form_class = ClientesForm    
    success_url = reverse_lazy('Administracion:ListarCliente')
#Fin de Vistas de CRUD Clientes

# Vistas para el CRUD de Celulares
class ListarCelulares(ListView):
	template_name = 'Administracion/celulares/celulares_list_form.html'
	model = Celulares
	
	def get_queryset(self):
		return Celulares.objects.all()

class CrearCelulares(CreateView):
	template_name='Administracion/celulares/celulares_create_form.html'
	form_class = CelularesForm
	success_url = reverse_lazy('Administracion:ListarCelulares')

class ActualizarCelulares(UpdateView):
    model = Celulares
    form_class = CelularesForm
    template_name_suffix = '/celulares_update_form'
    success_url = reverse_lazy('Administracion:ListarCelulares')

class EliminarCelulares(DeleteView):
    template_name='Administracion/celulares/celulares_confirm_delete_form.html'	
    model = Celulares
    form_class = CelularesForm    
    success_url = reverse_lazy('Administracion:ListarCelulares')
#Fin de Vistas de CRUD Celulares

# Vistas para el CRUD de Chips
class ListarChips(ListView):
	template_name = 'Administracion/chips/chips_list_form.html'
	model = Chips
	
	def get_queryset(self):
		return Chips.objects.all()

class CrearChips(CreateView):
	template_name='Administracion/chips/chips_create_form.html'
	form_class = ChipsForm
	success_url = reverse_lazy('Administracion:ListarChips')

class ActualizarChips(UpdateView):
    model = Chips
    form_class = ChipsForm
    template_name_suffix = '/chips_update_form'
    success_url = reverse_lazy('Administracion:ListarChips')

class EliminarChips(DeleteView):
    template_name='Administracion/chips/chips_confirm_delete_form.html'	
    model = Chips
    form_class = ChipsForm    
    success_url = reverse_lazy('Administracion:ListarChips')
#Fin de Vistas de CRUD Chips

# Vistas para el CRUD de Reparaciones
class ListarReparaciones(ListView):
    template_name = 'Administracion/reparaciones/reparaciones_list_form.html'
    model = Reparaciones
    
    def get_queryset(self):
        return Reparaciones.objects.all()

class CrearReparaciones(CreateView):
    template_name='Administracion/reparaciones/reparaciones_create_form.html'
    form_class = ReparacionesForm
    success_url = reverse_lazy('Administracion:ListarReparaciones')

class ActualizarReparaciones(UpdateView):
    model = Reparaciones
    form_class = ReparacionesForm
    template_name_suffix = '/reparaciones_update_form'
    success_url = reverse_lazy('Administracion:ListarReparaciones')

class EliminarReparaciones(DeleteView):
    template_name='Administracion/reparaciones/reparaciones_confirm_delete_form.html' 
    model = Reparaciones
    form_class = ReparacionesForm    
    success_url = reverse_lazy('Administracion:ListarReparaciones')
#Fin de Vistas de CRUD Reparaciones

# Vistas para el CRUD de Repuestos
class ListarRepuestos(ListView):
    template_name = 'Administracion/repuestos/repuestos_list_form.html'
    model = Repuestos
    
    def get_queryset(self):
        return Repuestos.objects.all()

class CrearRepuestos(CreateView):
    template_name='Administracion/repuestos/repuestos_create_form.html'
    form_class = RepuestosForm
    success_url = reverse_lazy('Administracion:ListarRepuestos')

class ActualizarRepuestos(UpdateView):
    model = Repuestos
    form_class = RepuestosForm
    template_name_suffix = '/repuestos_update_form'
    success_url = reverse_lazy('Administracion:ListarRepuestos')

class EliminarRepuestos(DeleteView):
    template_name='Administracion/repuestos/repuestos_confirm_delete_form.html' 
    model = Repuestos
    form_class = RepuestosForm    
    success_url = reverse_lazy('Administracion:ListarRepuestos')
#Fin de Vistas de CRUD Repuestos

# Vistas para el CRUD de Ventas
class ListarVentas(ListView):
    template_name = 'Administracion/ventas/ventas_list_form.html'
    model = Ventas
    
    def get_queryset(self):
        return Ventas.objects.all()

class CrearVentas(CreateView):
    template_name='Administracion/ventas/ventas_create_form.html'
    form_class = VentasForm
    success_url = reverse_lazy('Administracion:ListarVentas')

class ActualizarVentas(UpdateView):
    model = Ventas
    form_class = VentasForm
    template_name_suffix = '/ventas_update_form'
    success_url = reverse_lazy('Administracion:ListarVentas')

class EliminarVentas(DeleteView):
    template_name='Administracion/ventas/ventas_confirm_delete_form.html' 
    model = Ventas
    form_class = VentasForm    
    success_url = reverse_lazy('Administracion:ListarVentas')
#Fin de Vistas de CRUD Ventas

def generar_pdf_clientes(request):
    pdf_name = "Clientes.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    response = HttpResponse(content_type='application/pdf')
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
               pagesize=letter,
               rightMargin=20,
               leftMargin=20,
               topMargin=20,
               bottomMargin=20,
               )
    clientes = []
    styles = getSampleStyleSheet()
    header = Paragraph("Asociación Gissell", styles['Heading1'])
    t = Paragraph("Listado de personas", styles['Heading1'])

    clientes.append(header)
    clientes.append(t)
    headings = ('Id','Nombre', 'Apellido', 'Correo', 'Teléfono', 'Dirección')
    allclientes = [(c.id, c.nombre, c.apellido, c.email, c.telefono, c.direccion) for c in Clientes.objects.all()]
    t = Table([headings] + allclientes, colWidths=[1 * cm, 3 * cm, 3 * cm, 6 * cm, 2 * cm, 4 * cm] )
    t.setStyle(TableStyle(
        [
               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.darkblue),
               ('GRID', (0, 0), (5, -1), 1, colors.dodgerblue),
               ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    clientes.append(t)
    doc.build(clientes)
    response.write(buff.getvalue())
    buff.close()
    return response