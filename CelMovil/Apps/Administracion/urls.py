"""CelMovil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path
from .views import HomeView, ListarAccesorio, CrearAccesorio, ActualizarAccesorio, EliminarAccesorio, ListarEmpleados, \
    CrearEmpleados, ActualizarEmpleados, EliminarEmpleados, ListarCliente, CrearCliente, ActualizarCliente, EliminarCliente, \
    ListarCelulares, CrearCelulares, ActualizarCelulares, EliminarCelulares, ListarChips, CrearChips, ActualizarChips, \
    EliminarChips, ListarReparaciones, CrearReparaciones, ActualizarReparaciones, EliminarReparaciones, ListarRepuestos, \
    CrearRepuestos, ActualizarRepuestos, EliminarRepuestos, ListarVentas, CrearVentas, ActualizarVentas, EliminarVentas, \
    generar_pdf_clientes 

app_name = 'Administracion'

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='Home'),
    # Urls de Accesorios
    path('ListarAccesorio/', login_required(ListarAccesorio.as_view()), name='ListarAccesorio'),
    path('CrearAccesorio/', login_required(CrearAccesorio.as_view()), name='CrearAccesorio'),
    path('ActualizarAccesorio/<int:pk>/', login_required(ActualizarAccesorio.as_view()), name='ActualizarAccesorio'),
    path('EliminarAccesorio/<int:pk>/', login_required(EliminarAccesorio.as_view()), name='EliminarAccesorio'),
    # Fin de urls de Accesorios
    
    # Urls de Empleados
    path('ListarEmpleados/', login_required(ListarEmpleados.as_view()), name='ListarEmpleados'),
    path('CrearEmpleados/', login_required(CrearEmpleados.as_view()), name='CrearEmpleados'),
    path('ActualizarEmpleados/<int:pk>/', login_required(ActualizarEmpleados.as_view()), name='ActualizarEmpleados'),
    path('EliminarEmpleados/<int:pk>/', login_required(EliminarEmpleados.as_view()), name='EliminarEmpleados'),
    # Fin de urls de Empleados

    # Urls de Clientes
    path('ListarCliente/', login_required(ListarCliente.as_view()), name='ListarCliente'),
    path('CrearCliente/', login_required(CrearCliente.as_view()), name='CrearCliente'),
    path('ActualizarCliente/<int:pk>/', login_required(ActualizarCliente.as_view()), name='ActualizarCliente'),
    path('EliminarCliente/<int:pk>/', login_required(EliminarCliente.as_view()), name='EliminarCliente'),
    # Fin de urls de Clientes

    # Urls de Celulares
    path('ListarCelulares/', login_required(ListarCelulares.as_view()), name='ListarCelulares'),
    path('CrearCelulares/', login_required(CrearCelulares.as_view()), name='CrearCelulares'),
    path('ActualizarCelulares/<int:pk>/', login_required(ActualizarCelulares.as_view()), name='ActualizarCelulares'),
    path('EliminarCelulares/<int:pk>/', login_required(EliminarCelulares.as_view()), name='EliminarCelulares'),
    # Fin de urls de Celulares

    # Urls de Chips
    path('ListarChips/', login_required(ListarChips.as_view()), name='ListarChips'),
    path('CrearChips/', login_required(CrearChips.as_view()), name='CrearChips'),
    path('ActualizarChips/<int:pk>/', login_required(ActualizarChips.as_view()), name='ActualizarChips'),
    path('EliminarChips/<int:pk>/', login_required(EliminarChips.as_view()), name='EliminarChips'),
    # Fin de urls de Chips

    # Urls de Reparaciones
    path('ListarReparaciones/', login_required(ListarReparaciones.as_view()), name='ListarReparaciones'),
    path('CrearReparaciones/', login_required(CrearReparaciones.as_view()), name='CrearReparaciones'),
    path('ActualizarReparaciones/<int:pk>/', login_required(ActualizarReparaciones.as_view()), name='ActualizarReparaciones'),
    path('EliminarReparaciones/<int:pk>/', login_required(EliminarReparaciones.as_view()), name='EliminarReparaciones'),
    # Fin de urls de Reparaciones

    # Urls de Repuestos
    path('ListarRepuestos/', login_required(ListarRepuestos.as_view()), name='ListarRepuestos'),
    path('CrearRepuestos/', login_required(CrearRepuestos.as_view()), name='CrearRepuestos'),
    path('ActualizarRepuestos/<int:pk>/', login_required(ActualizarRepuestos.as_view()), name='ActualizarRepuestos'),
    path('EliminarRepuestos/<int:pk>/', login_required(EliminarRepuestos.as_view()), name='EliminarRepuestos'),
    # Fin de urls de Repuestos

    # Urls de Ventas
    path('ListarVentas/', login_required(ListarVentas.as_view()), name='ListarVentas'),
    path('CrearVentas/', login_required(CrearVentas.as_view()), name='CrearVentas'),
    path('ActualizarVentas/<int:pk>/', login_required(ActualizarVentas.as_view()), name='ActualizarVentas'),
    path('EliminarVentas/<int:pk>/', login_required(EliminarVentas.as_view()), name='EliminarVentas'),
    # Fin de urls de Ventas

    # Reporte
    path('reporte-cliente', login_required(generar_pdf_clientes), name='reporte_cliente'),
]