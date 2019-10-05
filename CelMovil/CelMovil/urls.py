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
from django.urls import include, path

urlpatterns = [
    path('', include('Apps.Principal.urls')),
<<<<<<< HEAD
    path('administracion/', include('Apps.Administracion.urls', namespace = 'administracion')),
=======
    path('Administracion/', include('Apps.Administracion.urls')),
>>>>>>> a2ca7c166c5a9c678fc83e255510e961790f230b
    path('admin/', admin.site.urls),    
]
