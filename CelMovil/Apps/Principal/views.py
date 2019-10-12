from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name='Principal/index.html'

class ProductosView(TemplateView):
    template_name='Principal/productos.html'

class OfertasView(TemplateView):
    template_name='Principal/ofertas.html'

class ContactoView(TemplateView):
    template_name='Principal/contacto.html'

class InicioView(TemplateView):
    template_name='Principal/inicio.html'