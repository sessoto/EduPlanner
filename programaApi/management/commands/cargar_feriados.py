from django.core.management.base import BaseCommand
from eventos.models import Evento
from programaApi.servicios import obtener_feriados
from datetime import date


class Command(BaseCommand):
    help = 'Carga feriados desde la API externa'

    def add_arguments(self, parser):
        parser.add_argument(
            '--año',
            type=int,
            default=2024, 
            help='Año para el que se cargarán los feriados'
        )

    def handle(self, *args, **kwargs):
        año = kwargs['año']  # Obtener el año de los argumentos
        self.stdout.write(f"Cargando feriados para el año {año}...")

        datos = obtener_feriados(año)
        if "error" in datos:
            self.stdout.write(self.style.ERROR(datos["error"]))
        else:
            
            for feriado in datos.get("response", {}).get("holidays", []):
                try:
                    
                    año = feriado["date"]["datetime"]["year"]
                    mes = feriado["date"]["datetime"]["month"]
                    día = feriado["date"]["datetime"]["day"]

                   
                    fecha_formateada = date(año, mes, día)

                    
                    Evento.objects.get_or_create(
                        nombre=feriado["name"],
                        descripcion=feriado.get("description", ""),
                        fecha_inicio=fecha_formateada,
                        fecha_fin=fecha_formateada,
                        es_feriado=True
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error procesando el feriado {feriado['name']}: {e}"))
            
            self.stdout.write(self.style.SUCCESS(f'Feriados para el año {año} cargados correctamente.'))