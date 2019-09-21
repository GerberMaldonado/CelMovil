from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
	template_name='Principal/index.html'

class BaseView(TemplateView):
	template_name='Principal/base.html'

class ProductosView(TemplateView):
	template_name='Principal/productos.html'

class OfertasView(TemplateView):
	template_name='Principal/ofertas.html'

class ContactoView(TemplateView):
	template_name='Principal/contacto.html'