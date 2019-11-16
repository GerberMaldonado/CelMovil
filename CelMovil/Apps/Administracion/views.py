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
from .models import Accesorio, Empleado, Cliente, Celular, Chip, Reparacion, Repuesto, Venta
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import render
from django.db.models import Count
# Create your views here.

class HomeView(TemplateView):
	template_name='Administracion/home.html'

# Vistas para el CRUD de Accesorios
class ListarAccesorio(ListView):
	template_name_suffix = '/accesorios_list_form'
	model = Accesorio	
	def get_queryset(self):
		return Accesorio.objects.all()

class CrearAccesorio(CreateView):
	template_name='Administracion/accesorio/accesorios_create_form.html'
	form_class = AccesoriosForm
	success_url = reverse_lazy('Administracion:ListarAccesorio')

class ActualizarAccesorio(UpdateView):
    model = Accesorio
    form_class = AccesoriosForm
    template_name_suffix = '/accesorios_update_form'
    success_url = reverse_lazy('Administracion:ListarAccesorio')

class EliminarAccesorio(DeleteView):
    template_name_suffix='/accesorios_confirm_delete_form'	
    model = Accesorio
    form_class = AccesoriosForm    
    success_url = reverse_lazy('Administracion:ListarAccesorio')
#Fin de Vistas de CRUD Accesorios

# Vistas para el CRUD de Empleados
class ListarEmpleados(ListView):
    template_name_suffix = '/empleados_list_form'
    model = Empleado    
    def get_queryset(self):
        return Empleado.objects.all()

class CrearEmpleados(CreateView):
    template_name='Administracion/empleado/empleados_create_form.html'
    form_class = EmpleadosForm
    success_url = reverse_lazy('Administracion:ListarEmpleados')

class ActualizarEmpleados(UpdateView):
    model = Empleado
    form_class = EmpleadosForm
    template_name_suffix = '/empleados_update_form'
    success_url = reverse_lazy('Administracion:ListarEmpleados')

class EliminarEmpleados(DeleteView):
    template_name_suffix='/empleados_confirm_delete_form'   
    model = Empleado
    form_class = EmpleadosForm    
    success_url = reverse_lazy('Administracion:ListarEmpleados')
#Fin de Vistas de CRUD Empleados

# Vistas para el CRUD de Clientes
class ListarCliente(ListView):
	template_name_suffix = '/clientes_list_form'
	model = Cliente	
	def get_queryset(self):
		return Cliente.objects.all()

def showthis(request):    
    count= Cliente.objects.annotate(Count('id'))  
    context= {'count': count}        
    return render(request, 'Administracion/home.html', context) 

class CrearCliente(CreateView):
	template_name='Administracion/cliente/clientes_create_form.html'
	form_class = ClientesForm
	success_url = reverse_lazy('Administracion:ListarCliente')

class ActualizarCliente(UpdateView):
    model = Cliente
    form_class = ClientesForm
    template_name_suffix = '/clientes_update_form'
    success_url = reverse_lazy('Administracion:ListarCliente')

class EliminarCliente(DeleteView):
    template_name_suffix='/clientes_confirm_delete_form'	
    model = Cliente
    form_class = ClientesForm    
    success_url = reverse_lazy('Administracion:ListarCliente')
#Fin de Vistas de CRUD Clientes

# Vistas para el CRUD de Celulares
class ListarCelulares(ListView):
	template_name_suffix = '/celulares_list_form'
	model = Celular	
	def get_queryset(self):
		return Celular.objects.all()

class CrearCelulares(CreateView):
	template_name='Administracion/celulare/celulares_create_form.html'
	form_class = CelularesForm
	success_url = reverse_lazy('Administracion:ListarCelulares')

class ActualizarCelulares(UpdateView):
    model = Celular
    form_class = CelularesForm
    template_name_suffix = '/celulares_update_form'
    success_url = reverse_lazy('Administracion:ListarCelulares')

class EliminarCelulares(DeleteView):
    template_name_suffix='/celulares_confirm_delete_form'	
    model = Celular
    form_class = CelularesForm    
    success_url = reverse_lazy('Administracion:ListarCelulares')
#Fin de Vistas de CRUD Celulares

# Vistas para el CRUD de Chips
class ListarChips(ListView):
	template_name_suffix = '/chips_list_form'
	model = Chip
	def get_queryset(self):
		return Chip.objects.all()

class CrearChips(CreateView):
	template_name='Administracion/chip/chips_create_form.html'
	form_class = ChipsForm
	success_url = reverse_lazy('Administracion:ListarChips')

class ActualizarChips(UpdateView):
    model = Chip
    form_class = ChipsForm
    template_name_suffix = '/chips_update_form'
    success_url = reverse_lazy('Administracion:ListarChips')

class EliminarChips(DeleteView):
    template_name_suffix='/chips_confirm_delete_form'	
    model = Chip
    form_class = ChipsForm    
    success_url = reverse_lazy('Administracion:ListarChips')
#Fin de Vistas de CRUD Chips

# Vistas para el CRUD de Reparaciones
class ListarReparaciones(ListView):
    template_name_suffix = '/reparaciones_list_form'
    model = Reparacion
    def get_queryset(self):
        return Reparacion.objects.all()

class CrearReparaciones(CreateView):
    template_name='Administracion/reparacion/reparaciones_create_form.html'
    form_class = ReparacionesForm
    success_url = reverse_lazy('Administracion:ListarReparaciones')

class ActualizarReparaciones(UpdateView):
    model = Reparacion
    form_class = ReparacionesForm
    template_name_suffix = '/reparaciones_update_form'
    success_url = reverse_lazy('Administracion:ListarReparaciones')

class EliminarReparaciones(DeleteView):
    template_name_suffix='/reparaciones_confirm_delete_form' 
    model = Reparacion
    form_class = ReparacionesForm    
    success_url = reverse_lazy('Administracion:ListarReparaciones')
#Fin de Vistas de CRUD Reparaciones

# Vistas para el CRUD de Repuestos
class ListarRepuestos(ListView):
    template_name_suffix = '/repuestos_list_form'
    model = Repuesto    
    def get_queryset(self):
        return Repuesto.objects.all()

class CrearRepuestos(CreateView):
    template_name='Administracion/repuesto/repuestos_create_form.html'
    form_class = RepuestosForm
    success_url = reverse_lazy('Administracion:ListarRepuestos')

class ActualizarRepuestos(UpdateView):
    model = Repuesto
    form_class = RepuestosForm
    template_name_suffix = '/repuestos_update_form'
    success_url = reverse_lazy('Administracion:ListarRepuestos')

class EliminarRepuestos(DeleteView):
    template_name_suffix='/repuestos_confirm_delete_form' 
    model = Repuesto
    form_class = RepuestosForm    
    success_url = reverse_lazy('Administracion:ListarRepuestos')
#Fin de Vistas de CRUD Repuestos

# Vistas para el CRUD de Ventas
class ListarVentas(ListView):
    template_name_suffix = '/ventas_list_form'
    model = Venta    
    def get_queryset(self):
        return Venta.objects.all()

class CrearVentas(CreateView):
    template_name='Administracion/venta/ventas_create_form.html'
    form_class = VentasForm
    success_url = reverse_lazy('Administracion:ListarVentas')

class ActualizarVentas(UpdateView):
    model = Venta
    form_class = VentasForm
    template_name_suffix = '/ventas_update_form'
    success_url = reverse_lazy('Administracion:ListarVentas')

class EliminarVentas(DeleteView):
    template_name_suffix='/ventas_confirm_delete_form' 
    model = Venta
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
    header = Paragraph("Empresa CelMovil", styles['Heading1'])
    t = Paragraph("Listado de Clientes", styles['Heading1'])

    clientes.append(header)
    clientes.append(t)
    headings = ('Id','Nombre', 'Apellido', 'Correo', 'Teléfono', 'Dirección')
    allclientes = [(c.id, c.nombre, c.apellido, c.email, c.telefono, c.direccion) for c in Cliente.objects.all()]
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

def generar_pdf_celulares(request):
    pdf_name = "Celulares.pdf"  # llamado clientes
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
    header = Paragraph("Empresa CelMovil", styles['Heading1'])
    t = Paragraph("Listado de Celulares", styles['Heading1'])

    clientes.append(header)
    clientes.append(t)
    headings = ('Id','Codigo', 'Marca', 'Serie Imei', 'Precio Mayor', 'Precio Unidad')
    allclientes = [(c.id, c.codigo, c.marca, c.serieimei, c.preciomayor, c.preciounidad) for c in Celular.objects.all()]
    t = Table([headings] + allclientes, colWidths=[1 * cm, 3 * cm, 3 * cm, 4 * cm, 4 * cm, 4 * cm] )
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

def generar_pdf_accesorios(request):
    pdf_name = "Celulares.pdf"  # llamado clientes
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
    header = Paragraph("Empresa CelMovil", styles['Heading1'])
    t = Paragraph("Listado de Accesorios", styles['Heading1'])

    clientes.append(header)
    clientes.append(t)
    headings = ('Id','Codigo', 'Nombre', 'Marca', 'Cantidad', 'Fecha Cración')
    allclientes = [(c.id, c.codigo, c.nombre, c.marca, c.cantidad, c.creacion) for c in Accesorio.objects.all()]
    t = Table([headings] + allclientes, colWidths=[1 * cm, 3 * cm, 3 * cm, 3 * cm, 2 * cm, 7 * cm] )
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

def generar_pdf_chips(request):
    pdf_name = "Celulares.pdf"  # llamado clientes
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
    header = Paragraph("Empresa CelMovil", styles['Heading1'])
    t = Paragraph("Listado de Chips", styles['Heading1'])

    clientes.append(header)
    clientes.append(t)
    headings = ('Id','Codigo', 'Operador', 'Serie')
    allclientes = [(c.id, c.codigo, c.operador, c.serie) for c in Chip.objects.all()]
    t = Table([headings] + allclientes, colWidths=[1 * cm, 5 * cm, 5 * cm, 5 * cm] )
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

def generar_pdf_reparaciones(request):
    pdf_name = "Celulares.pdf"  # llamado clientes
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
    header = Paragraph("Empresa CelMovil", styles['Heading1'])
    t = Paragraph("Listado de Reparaciones", styles['Heading1'])

    clientes.append(header)
    clientes.append(t)
    headings = ('Id','Descripción', 'Costo', 'Cliente')
    allclientes = [(c.id, c.descripcionfalla, c.costo, c.clientes) for c in Reparacion.objects.all()]
    t = Table([headings] + allclientes, colWidths=[1 * cm, 8 * cm, 3 * cm, 3 * cm] )
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

def generar_pdf_repuestos(request):
    pdf_name = "Celulares.pdf"  # llamado clientes
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
    header = Paragraph("Empresa CelMovil", styles['Heading1'])
    t = Paragraph("Listado de Repuestos", styles['Heading1'])

    clientes.append(header)
    clientes.append(t)
    headings = ('Id','Marca', 'Modelo', 'Cantidad', 'Precio')
    allclientes = [(c.id, c.nombre, c.marca, c.modelo, c.cantidad) for c in Repuesto.objects.all()]
    t = Table([headings] + allclientes, colWidths=[1 * cm, 4 * cm, 4 * cm, 4 * cm, 3 * cm] )
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

def generar_pdf_empleados(request):
    pdf_name = "Celulares.pdf"  # llamado clientes
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
    header = Paragraph("Empresa CelMovil", styles['Heading1'])
    t = Paragraph("Listado de Empleados", styles['Heading1'])

    clientes.append(header)
    clientes.append(t)
    headings = ('Id','Nombre', 'Apellido', 'Email', 'Dpi', 'Rol')
    allclientes = [(c.id, c.nombre, c.apellido, c.email, c.dpi, c.rol) for c in Empleado.objects.all()]
    t = Table([headings] + allclientes, colWidths=[1 * cm, 3 * cm, 3 * cm, 6 * cm, 3 * cm, 3 * cm] )
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