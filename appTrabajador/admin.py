from django.contrib import admin
from appTrabajador.models import Cargo, Trabajador

# Register your models here.

class CargoAdmin(admin.ModelAdmin):
    list_display = ('nombre_cargo', 'descripcion')
    search_fields = ('nombre_cargo',)

admin.site.register(Cargo, CargoAdmin)

class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('nombre_trabajador', 'cargo', 'telefono', 'direccion', 'ci')
    search_fields = ('nombre_trabajador', 'ci')
    list_filter = ('cargo',)

admin.site.register(Trabajador, TrabajadorAdmin)
