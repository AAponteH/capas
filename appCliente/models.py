from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_cliente