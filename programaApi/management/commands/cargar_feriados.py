from django.core.management.base import BaseCommand
from eventos.models import Evento
from programaApi.servicios import obtener_feriados
from django.conf import settings

class Command(BaseCommand):
    help = 'Carga feriados desde la API externa'

    def handle(self, *args, **kwargs):
        datos = obtener_feriados(settings.API_URL, settings.API_KEY)
        if "error" in datos:
            self.stdout.write(self.style.ERROR(datos["error"]))
        else:
            for feriado in datos.get("feriados", []):
                Evento.objects.get_or_create(
                    nombre=feriado["nombre"],
                    descripcion=feriado.get("descripcion", ""),
                    fecha_inicio=feriado["fecha"],
                    fecha_fin=feriado["fecha"],
                    es_feriado=True
                )
            self.stdout.write(self.style.SUCCESS('Feriados cargados correctamente.'))