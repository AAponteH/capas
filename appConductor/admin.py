from django.contrib import admin
from appConductor.models import Conductor
# Register your models here.
class ConductorAdmin(admin.ModelAdmin):
    list_display = ('nombre_conductor', 'telefono', 'direccion')
    search_fields = ('nombre_conductor')
admin.site.register(Conductor, ConductorAdmin)
