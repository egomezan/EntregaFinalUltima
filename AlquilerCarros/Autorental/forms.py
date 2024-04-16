from django import forms

from .models import Carro, Reserva


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

# class SalaCreateForm(forms.ModelForm):
#     class Meta:
#         model = Sala
#         fields = ['nombre', 'disponible', 'capacidad', 'descripcion']
#         labels = {
#             'nombre': 'Elegir un nombre para la Sala',
#             'disponible': 'Disponible',
#             'capacidad': 'Capacidad máxima',
#             'descripcion': 'Descripción',
#         }


