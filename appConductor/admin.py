from django.contrib import admin
from appConductor.models import Conductor
# Register your models here.
class ConductorAdmin(admin.ModelAdmin):
    list_display = ('nombre_conductor', 'ci', 'telefono')
    search_fields = ('nombre_conductor', 'ci')

admin.site.register(Conductor, ConductorAdmin)
