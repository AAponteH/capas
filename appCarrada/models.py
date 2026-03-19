from django.db import models
from django.utils import timezone
from datetime import datetime
from django.apps import apps

# Create your models here.
class Carrada(models.Model):
    codigo_carrada = models.CharField(max_length=50, unique=True, blank=True, editable=False)
    conductor = models.ForeignKey('appConductor.Conductor', on_delete=models.CASCADE)
    lote = models.ForeignKey('appLote.Lote', on_delete=models.PROTECT, blank=True, null=True, editable=False)
    bidones_retirados = models.IntegerField()
    bidones_vacios = models.IntegerField(default=0)
    fecha_hora_carrada = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Generar codigo_carrada si no existe
        if not self.codigo_carrada:
            fecha = datetime.now().strftime("%Y%m%d")
            # Contar cuántas carradas existen para esta fecha
            carradas_hoy = Carrada.objects.filter(
                fecha_hora_carrada__date=datetime.now().date()
            ).count()
            numero_secuencial = carradas_hoy + 1
            self.codigo_carrada = f"C-{fecha}-{numero_secuencial:03d}"
        
        # Asignar lote del día si no existe
        if not self.lote:
            Lote = apps.get_model('appLote', 'Lote')
            self.lote = Lote.objects.filter(
                fecha_lote=datetime.now().date()
            ).first()
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.codigo_carrada
    
    def __str__(self):
        return self.codigo_carrada