from django.db import models

# Create your models here.
class Carrada(models.Model):
    conductor = models.ForeignKey('appConductor.Conductor', on_delete=models.CASCADE)
    cliente = models.ForeignKey('appCliente.Cliente', on_delete=models.CASCADE)
    bidones_retirados = models.IntegerField()
    bidones_vacios = models.IntegerField()
    fecha_hora_carrada = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.Codigo_carrada