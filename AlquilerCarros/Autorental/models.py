from django.db import models
from django.utils import timezone


class Carro(models.Model):
    TRANSMISSION_CHOICES = (
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    )
    marca = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    transmision = models.CharField(max_length=100, choices= TRANSMISSION_CHOICES)

    modelo = models.IntegerField()
   # descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Carro {self.marca}"

class Reserva(models.Model):
    nombre_de_usuario = models.CharField(max_length=50)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField(default=timezone.now)
    hora_inicio = models.TimeField(default=timezone.now)
    hora_fin = models.TimeField(default=timezone.now)
    descripcion = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.nombre_de_usuario}  - {self.fecha}"

class Seguro(models.Model):
    precio = models.IntegerField()
    cubreterceros = models.BooleanField(default=True)
    montoquecubre = models.IntegerField()
    nombreseguro = models.CharField(max_length=40)


    def __str__(self):
        return f"{self.nombreseguro} "
 

  #  def __str__(self):
       # return f"{self.nombre_de_usuario} - {self.carro.marca} - {self.carro.modelo}- {self.fecha}"

# class Reserva(models.Model):
#      nombre_de_usuario = models.CharField(max_length=50)
#      fecha = models.DateField(default=timezone.now)
#      hora_inicio = models.TimeField(default=timezone.now)
#      hora_fin = models.TimeField(default=timezone.now)
#      descripcion = models.TextField(blank=True, null=True)

#      def __str__(self):
#          return f"{self.nombre_de_usuario} - {self.fecha}"
    

