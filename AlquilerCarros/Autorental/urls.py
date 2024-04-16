

from django.contrib import admin
from django.urls import path
from .views import home_view, list_view, agregar_carro, detail_auto_view, crear_reserva, search_with_form_view, reservas_lista, segurosautos, crearseguro


urlpatterns = [
    path("", home_view),
    path("listofcars/", list_view),
    path("crear-carro-con-form/", agregar_carro, name ="yyy"),
    path("detail-carro/<auto_id>", detail_auto_view),
    path("crear-reserva-form/", crear_reserva, name="zzz"),
    path("buscar-con-formulario/", search_with_form_view, name="xyz"),
    path("listareservas/", reservas_lista, name="zyz"),
    path("seguros/", segurosautos),
    path("seguros/crear", crearseguro, name="jjj"),
  
]