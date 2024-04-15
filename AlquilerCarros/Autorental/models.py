from django.db import models


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
        return f"testing this shit {self.modelo}"


# class Reserva(models.Model):
#      nombre_de_usuario = models.CharField(max_length=50)
#      fecha = models.DateField(default=timezone.now)
#      hora_inicio = models.TimeField(default=timezone.now)
#      hora_fin = models.TimeField(default=timezone.now)
#      descripcion = models.TextField(blank=True, null=True)

#      def __str__(self):
#          return f"{self.nombre_de_usuario} - {self.fecha}"
    

# class Seguro(models.Model):
#     precio = models.CharField(max_length=100)
#     tipo = models.BooleanField(default=True)
#     montoquecubre = models.IntegerField()
#     descripcion = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.nombre} - {'Disponible' if self.disponible else 'No Disponible'} - Capacidad: {self.capacidad}"
 
