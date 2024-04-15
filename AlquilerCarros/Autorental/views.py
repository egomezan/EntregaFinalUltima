from django.shortcuts import render
# from .forms import ReservaCreateForm, ReservaSearchForm, SalaCreateForm

from .models import Carro

def home_view(request):
    return render(request,"autorental/home.html")



def list_view(request):
    reservas = Carro.objects.all()
    contexto_dict = {'Carro': reservas}
    return render(request, "autorental/list.html", contexto_dict)

# def list_view(request):
#     reservas = Reserva.objects.all()
#     contexto_dict = {'reservas': reservas}
#     return render(request, "Autorental/list.html", contexto_dict)


# def addc_carro_with_form_view(request):
#     if request.method == "GET":
#         contexto = {"LUISMIGUEL": SalaCreateForm()}
#         return render(request, "Autorental/form-create-sala.html", contexto)
#     elif request.method == "POST":
#         form = SalaCreateForm(request.POST)
#         if form.is_valid():
#             nombre = form.cleaned_data['nombre']
#             disponible = form.cleaned_data['disponible']
#             capacidad = form.cleaned_data['capacidad']
#             descripcion = form.cleaned_data['descripcion']
#             nueva_sala = Sala(nombre=nombre, disponible=disponible, capacidad=capacidad, descripcion=descripcion)
#             nueva_sala.save()
#             return detail_sala_view(request, nueva_sala.id)


# def search_view(request, nombre_de_usuario):
#     reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
#     contexto_dict = {"reservas": reservas_del_usuario}
#     return render(request, "bookings/list.html", contexto_dict)


# def create_view(request, nombre_de_usuario, sala):
#     reserva = Reserva.objects.create(nombre_de_usuario=nombre_de_usuario, sala=sala)
#     return HttpResponse(f"resultado: {reserva}")