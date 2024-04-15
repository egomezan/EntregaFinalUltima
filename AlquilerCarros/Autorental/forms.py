from django import forms

from .models import Carro


# class ReservaSearchForm(forms.Form):
#     nombre_de_usuario = forms.CharField(max_length=50, required=True, label="Ingresar nombre de usuario")


class CarroCreateForm(forms.Form):
   class Meta:
    model = Carro
    fields = ['Marca', 'Modelo', 'disponible', 'Transmision']
    
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


