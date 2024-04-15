from django.shortcuts import render
from .forms import CarroCreateForm

from django.http import HttpResponse
from .models import Carro

def home_view(request):
    return render(request,"autorental/home.html")



def list_view(request):
    carros = Carro.objects.all()
    contexto_dict = {'Carro': carros}
    return render(request, "autorental/list.html", contexto_dict)


def agregar_carro(request):
    if request.method == "GET":
        contexto = {"create_form": CarroCreateForm()}
        return render(request, "autorental/form-create-carro.html", contexto)
    elif request.method == "POST":
        form = CarroCreateForm(request.POST)
        if form.is_valid():
            marca = form.cleaned_data['marca']
            disponible = form.cleaned_data['disponible']
            modelo = form.cleaned_data['modelo']
            transmision = form.cleaned_data['transmision']
            nuevo_auto = Carro(marca=marca, disponible=disponible, modelo=modelo, transmision=transmision)
            nuevo_auto.save()
        return detail_auto_view(request, nuevo_auto.id)
  

def detail_auto_view(request, auto_id):
    auto = Carro.objects.get(id=auto_id)
    contexto_dict = {"Carro": auto}
    return render(request, "autorental/detail-auto.html", contexto_dict)

  
   # form = CarroCreateForm(request.POST)
    # carro = Carro.objects.create(modelo, marca, transmision)

    # return HttpResponse(f"El nuevo carro es {carro}")

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