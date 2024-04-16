"""
URL configuration for AlquilerCarros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from django.http import HttpResponse


def mi_funcion_que_es_una_vista_o_view(yy):
    return HttpResponse("<h1>Bienvenidos al Proyecto</h1>  <h2 > <a href= /autorental> IR A APLICACION</a> </h2>")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", mi_funcion_que_es_una_vista_o_view),
    path("autorental/", include("autorental.urls")),
   # path("bookings/", include("bookings.urls")), # conecto las URLS de `bookings` con las URLS generales
  #  path("sales/", include("sales.urls")), # conecto las URLS de `sales` con las URLS generales
]