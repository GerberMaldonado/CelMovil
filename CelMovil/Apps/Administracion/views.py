from django.views.generic import TemplateView

# Create your views here.
class AdminView(TemplateView):
	template_name='Administracion/index.html'