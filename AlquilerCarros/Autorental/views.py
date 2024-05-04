from django.shortcuts import render, redirect
from .forms import CarroCreateForm, ReservaCreateForm, ReservaSearchForm, SeguroCreateForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .models import Carro, Reserva, Seguro
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request,"autorental/home.html")



def list_view(request):
    carros = Carro.objects.all()
    contexto_dict = {'Carro': carros}
    return render(request, "autorental/list.html", contexto_dict)



def reservas_lista(request):
    reservas = Reserva.objects.all()
    contexto_dict = {'todas_las_reservas': reservas}
    return render(request, "autorental/lista.html", contexto_dict)

@login_required
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
  
@login_required  
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


def segurosautos(request):
     seguros = Seguro.objects.all()
     return render(request, 'seguros/lista_seguros.html', {'seguros': seguros})

@login_required
def crearseguro(request):
    if request.method == "GET":
        contexto = {"create_form": SeguroCreateForm()}
        return render(request, "autorental/form-create-seguro.html", contexto)
    elif request.method == "POST":
        form = SeguroCreateForm(request.POST)
        if form.is_valid():
            precio = form.cleaned_data['precio']
            cubreterceros = form.cleaned_data['cubreterceros']
            montoquecubre = form.cleaned_data['montoquecubre']
            nombreseguro = form.cleaned_data['nombreseguro']
            nuevo_seguro = Seguro(precio=precio, cubreterceros=cubreterceros, montoquecubre=montoquecubre, nombreseguro=nombreseguro)
            nuevo_seguro.save()
       # return HttpResponse('<p1> Seguro creado correctamente</p1>' )
        return redirect("home")


def carro_delete_view(request, carro_id):
    carro_a_borrar = Carro.objects.filter(id=carro_id).first()
    carro_a_borrar.delete()
    return redirect("carro_list")


def carro_update_view(request, carro_id):
    carro_a_editar = Carro.objects.filter(id=carro_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "marca": carro_a_editar.marca,
            "disponible": carro_a_editar.disponible,
            "modelo": carro_a_editar.modelo,
            "transmision": carro_a_editar.transmision,
        }
        formulario = CarroCreateForm(initial=valores_iniciales)
        contexto = {"formul": formulario, "objeto": carro_a_editar}
        return render(request, "autorental/form_update.html", contexto)
    elif request.method == "POST":
        form = CarroCreateForm(request.POST)
        if form.is_valid():
            marca = form.cleaned_data["marca"]
            disponible = form.cleaned_data["disponible"]
            modelo = form.cleaned_data["modelo"]
            transmision = form.cleaned_data["transmision"]
            carro_a_editar.marca = marca
            carro_a_editar.disponible = disponible
            carro_a_editar.modelo = modelo
            carro_a_editar.transmision = transmision
            carro_a_editar.save()
            return redirect("detail-carro", carro_a_editar.id)

def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, "autorental/login.html", {"MICHAELSTIPE": form})


def user_logout_view(request):
    logout(request)
    return redirect("login")



from django.contrib.auth.forms import UserCreationForm


def user_creation_view(request):
    if request.method == "GET":
        form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    return render(request, "autorental/crear_usuario.html", {"form": form})


def about_view(request):
    return render(request,"autorental/about_me.html")
