from django.contrib import admin
from .models import Eventos

@admin.register(Eventos)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion', 'fecha')
    search_fields = ('nombre',)