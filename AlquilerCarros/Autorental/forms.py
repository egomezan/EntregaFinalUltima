from django import forms

from .models import Carro, Reserva, Seguro


# class ReservaSearchForm(forms.Form):
#     nombre_de_usuario = forms.CharField(max_length=50, required=True, label="Ingresar nombre de usuario")


class CarroCreateForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['marca', 'modelo', 'disponible', 'transmision']
    
class ReservaCreateForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_de_usuario', 'carro', 'fecha', 'hora_inicio', 'hora_fin', 'descripcion'] 

class ReservaSearchForm(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=50, required=True, label="Ingrese nombre Usuario")

class SeguroCreateForm(forms.ModelForm):
    class Meta:
        model = Seguro
        fields = ['precio', 'cubreterceros', 'montoquecubre', 'nombreseguro']



