

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from .views import ( home_view, list_view, agregar_carro, 
                    detail_auto_view, crear_reserva, 
                    search_with_form_view, reservas_lista, 
                    segurosautos, crearseguro,  user_login_view,  user_logout_view,
                    user_creation_view, detail_view, carro_delete_view, carro_update_view,
                    about_view

)
urlpatterns = [
    path("", home_view, name="home"),
    path("listofcars/", list_view, name="carro_list"),
    path("crear-carro-con-form/", agregar_carro, name ="yyy"),
    path("detail-carro/<auto_id>", detail_auto_view, name="detail-carro"),
    path("crear-reserva-form/", crear_reserva, name="zzz"),
    path("buscar-con-formulario/", search_with_form_view, name="xyz"),
    path("listareservas/", reservas_lista, name="zyz"),
    path("seguros/", segurosautos),
    path("seguros/crear", crearseguro, name="jjj"),
    path("login/", user_login_view, name='login'),
    path("logout/", user_logout_view, name='logout'), 
    path("crear-usuario/", user_creation_view, name="crear-usuario"),
    path("detail-reserva/<reserva_id>", detail_view, name='list-reservas'),
    path("carro/delete/<carro_id>", carro_delete_view, name="carro-delete"),
    path("carro/update/<carro_id>", carro_update_view, name="carro-update"),
    path("about/", about_view, name="about_me")
 
]