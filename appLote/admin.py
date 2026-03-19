from django.contrib import admin
from appLote.models import Lote
# Register your models here.
class LoteAdmin(admin.ModelAdmin):
    list_display = ('codigo_lote', 'fecha_lote', 'trabajador_encargado', 'cantidad_producida')
    list_filter = ('fecha_lote', 'trabajador_encargado')
    search_fields = ('codigo_lote',)
    readonly_fields = ('codigo_lote', 'fecha_lote')
admin.site.register(Lote, LoteAdmin)