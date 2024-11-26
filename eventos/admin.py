from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'es_feriado')
    list_filter = ('es_feriado',)
    search_fields = ('nombre',)