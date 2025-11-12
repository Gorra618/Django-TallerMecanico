from django.contrib import admin
from .models import Presupuesto, Cotizacion

@admin.register(Presupuesto)
class PresupuestoAdmin(admin.ModelAdmin):
    list_display = ('monto', 'actualizado')

@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'unidades', 'precio', 'total')
    readonly_fields = ('total',)
