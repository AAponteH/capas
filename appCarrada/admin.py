from django.contrib import admin
from appCarrada.models import Carrada
# Register your models here.
class CarradaAdmin(admin.ModelAdmin):
    list_display = ('codigo_carrada', 'conductor', 'lote', 'bidones_retirados', 'bidones_vacios', 'fecha_hora_carrada')
    list_filter = ('fecha_hora_carrada',)
    search_fields = ('codigo_carrada',)
admin.site.register(Carrada, CarradaAdmin)