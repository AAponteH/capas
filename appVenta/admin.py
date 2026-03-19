from django.contrib import admin
from appVenta.models import Venta
# Register your models here.
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'conductor', 'cliente', 'lote', 'cantidad_vendida', 'bidones_recogidos', 'monto_total', 'fecha_hora_venta')
    list_filter = ('fecha_hora_venta', 'conductor', 'cliente')
    search_fields = ('conductor__nombre_conductor', 'cliente__nombre_cliente')
    readonly_fields = ('lote', 'monto_total', 'fecha_hora_venta')
admin.site.register(Venta, VentaAdmin)