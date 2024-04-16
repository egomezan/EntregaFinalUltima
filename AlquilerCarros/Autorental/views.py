from django.shortcuts import render
from .forms import CarroCreateForm, ReservaCreateForm, ReservaSearchForm

from django.http import HttpResponse
from .models import Carro, Reserva

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
  
  
def crear_reserva(request):
   if request.method == "GET":
       contexto = {"create_form": ReservaCreateForm()}
       return render(request, "autorental/form-create.html", contexto)
   elif request.method == "POST":
       form = ReservaCreateForm(request.POST)
       if form.is_valid():
           nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
           carro = form.cleaned_data['carro']
           fecha = form.cleaned_data['fecha']
           hora_inicio = form.cleaned_data['hora_inicio']
           hora_fin = form.cleaned_data['hora_fin']
           descripcion = form.cleaned_data['descripcion']
           nueva_reserva = Reserva(nombre_de_usuario=nombre_de_usuario, carro=carro, fecha=fecha, hora_inicio=hora_inicio, hora_fin=hora_fin, descripcion=descripcion)
           nueva_reserva.save()
       return detail_view(request, nueva_reserva.id)

def detail_auto_view(request, auto_id):
    auto = Carro.objects.get(id=auto_id)
    contexto_dict = {"Carro": auto}
    return render(request, "autorental/detail-auto.html", contexto_dict)



def detail_view(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    contexto_dict = {"reserva": reserva}
    return render(request, "autorental/detail.html", contexto_dict)


def search_with_form_view(request):
     if request.method == "GET":
        form = ReservaSearchForm()
        return render(request, "autorental/form-search.html", context={"search_form": form})
     elif request.method == "POST":
        #  devolverle a "chrome" la lista de reservas encontrada o avisar que no se encontró nada
        form = ReservaSearchForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
        reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
        contexto_dict = {"todas_las_reservas": reservas_del_usuario}
     return render(request, "autorental/lista.html", contexto_dict)
