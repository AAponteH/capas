from django.contrib import admin
from appTrabajador.models import Cargo, Trabajador

# Register your models here.

class CargoAdmin(admin.ModelAdmin):
    list_display = ('nombre_cargo', 'descripcion')
    search_fields = ('nombre_cargo',)

admin.site.register(Cargo, CargoAdmin)

class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('nombre_trabajador', 'ci', 'Cargo', 'telefono', 'fecha_contratacion')
    search_fields = ('nombre_trabajador', 'ci')
    list_filter = ('Cargo',)

admin.site.register(Trabajador, TrabajadorAdmin)
