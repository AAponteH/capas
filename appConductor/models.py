from django.db import models

# Create your models here.
class Conductor(models.Model):
    nombre_conductor = models.CharField(max_length=100)
    ci = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_conductor