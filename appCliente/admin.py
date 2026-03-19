from django.contrib import admin
from appCliente.models import Cliente
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'telefono', 'direccion')
    search_fields = ('nombre_cliente')
    list_filter = ('nombre_cliente',)

admin.site.register(Cliente, ClienteAdmin)
