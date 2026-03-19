from django.db import models
from datetime import datetime

# Create your models here.
class Lote(models.Model):
    codigo_lote = models.CharField(max_length=50, unique=True, blank=True, editable=False)
    fecha_lote = models.DateField(auto_now_add=True)
    trabador_encargado = models.ForeignKey('appTrabajador.Trabajador', on_delete=models.PROTECT)
    cantidad_producida = models.IntegerField()
    
    
    def save(self, *args, **kwargs):
        # Generar codigo_lote si no existe
        if not self.codigo_lote:
            fecha = datetime.now().strftime("%Y%m%d")
            # Contar cuántos lotes existen para esta fecha
            lotes_hoy = Lote.objects.filter(
                fecha_lote=datetime.now().date()
            ).count()
            numero_secuencial = lotes_hoy + 1
            self.codigo_lote = f"L-{fecha}-{numero_secuencial:03d}"
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.codigo_lote