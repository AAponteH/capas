from django.db import models

# Create your models here.
class Venta(models.Model):
    conductor = models.ForeignKey('appConductor.Conductor', on_delete=models.CASCADE)
    cliente = models.ForeignKey('appCliente.Cliente', on_delete=models.CASCADE)
    lote = models.ForeignKey('appLote.Lote', on_delete=models.CASCADE)
    cantidad_vendida = models.IntegerField()
    bidones_recogidos = models.IntegerField()
    monto_total = models.IntegerField()
    fecha_hora_venta = models.DateTimeField(auto_now_add=True)
