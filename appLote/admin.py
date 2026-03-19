from django.contrib import admin
from appLote.models import Lote
# Register your models here.
class LoteAdmin(admin.ModelAdmin):
    list_display = ('codigo_lote', 'fecha_lote', 'trabador_encargado', 'cantidad_producida')
    list_filter = ('fecha_lote',)
    search_fields = ('codigo_lote',)
admin.site.register(Lote, LoteAdmin)