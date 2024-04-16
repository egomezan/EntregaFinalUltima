

from django.contrib import admin
from django.urls import path
from .views import home_view, list_view, agregar_carro, detail_auto_view, crear_reserva, search_with_form_view, reservas_lista


urlpatterns = [
    path("", home_view),
    path("listofcars/", list_view),
    path("crear-carro-con-form/", agregar_carro, name ="yyy"),
    path("detail-carro/<auto_id>", detail_auto_view),
    path("crear-reserva-form/", crear_reserva, name="zzz"),
    path("buscar-con-formulario/", search_with_form_view, name="xyz"),
    path("listareservas/", reservas_lista, name="zyz"),

   # path("agregar/", agregar_carro),
#     path("carro/add/", create_sala_with_form_view, name="sala-create"),
#   #  path("nombreclientes/", nombre_clientes),
#    # path("bookings/", include("bookings.urls")), # conecto las URLS de `bookings` con las URLS generales
  #  path("sales/", include("sales.urls")), # conecto las URLS de `sales` con las URLS generales
]