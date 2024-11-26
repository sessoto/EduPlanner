from django.http import JsonResponse
from eventos.models import Evento

def api_eventos(request):
    eventos = Evento.objects.all()
    data = {
        "eventos": [
            {
                "nombre": evento.nombre,
                "descripcion": evento.descripcion,
                "fecha": evento.fecha_inicio.isoformat(),
                "es_feriado": evento.es_feriado,
            }
            for evento in eventos
        ]
    }
    return JsonResponse(data)
from django.shortcuts import render

def calendario(request):
    return render(request, 'eventos/calendario.html')

