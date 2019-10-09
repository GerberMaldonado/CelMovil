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
from django.contrib import admin
from django.urls import path
from .views import HomeView, ListarAccesorio, CrearAccesorio, ActualizarAccesorio, EliminarAccesorio, ListarCliente

app_name = 'Administracion'

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    # Urls de Accesorios
    path('ListarAccesorio/', ListarAccesorio.as_view(), name='ListarAccesorio'),
    path('CrearAccesorio/', CrearAccesorio.as_view(), name='CrearAccesorio'),
    path('ActualizarAccesorio/<int:pk>/', ActualizarAccesorio.as_view(), name='ActualizarAccesorio'),
    path('EliminarAccesorio/<int:pk>/', EliminarAccesorio.as_view(), name='EliminarAccesorio'),
    # Fin de urls de Accesorios

    # Urls de Accesorios
    path('ListarCliente/', ListarCliente.as_view(), name='ListarCliente'),
    #path('CrearAccesorio/', CrearAccesorio.as_view(), name='CrearAccesorio'),
    #path('ActualizarAccesorio/<int:pk>/', ActualizarAccesorio.as_view(), name='ActualizarAccesorio'),
    #path('EliminarAccesorio/<int:pk>/', EliminarAccesorio.as_view(), name='EliminarAccesorio'),
    # Fin de urls de Accesorios
]