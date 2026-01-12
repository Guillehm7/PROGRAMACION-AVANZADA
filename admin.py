from django.contrib import admin
from .models import PlatoTipico

@admin.register(PlatoTipico)
class PlatoTipicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region', 'precio_sugerido')
    list_filter = ('region',)
    search_fields = ('nombre',)
