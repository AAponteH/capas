from django.db import models

# Create your models here.
class Lote(models.Model):
    fecha_lote = models.DateField(auto_now_add=True)
    Codigo_lote = models.CharField(max_length=20, unique=True)
    trabador_encargado = models.CharField(max_length=100)
    cantidad_producida = models.IntegerField()
    Tamano_lote = models.IntegerField()
    def __str__(self):
        return self.Codigo_lote