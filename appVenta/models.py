from django.db import models
from datetime import datetime
from django.apps import apps

# Create your models here.
class Venta(models.Model):
    conductor = models.ForeignKey('appConductor.Conductor', on_delete=models.CASCADE)
    cliente = models.ForeignKey('appCliente.Cliente', on_delete=models.CASCADE)
    lote = models.ForeignKey('appLote.Lote', on_delete=models.PROTECT, blank=True, null=True, editable=False)
    cantidad_vendida = models.IntegerField()
    bidones_recogidos = models.IntegerField()
    monto_total = models.IntegerField(default=0, editable=False)
    fecha_hora_venta = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # Asignar lote del día si no existe
        if not self.lote:
            Lote = apps.get_model('appLote', 'Lote')
            self.lote = Lote.objects.filter(
                fecha_lote=datetime.now().date()
            ).first()
        
        # Calcular monto_total: cada bidón vale 8
        self.monto_total = self.bidones_recogidos * 8
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Venta {self.id} - {self.cliente}"
