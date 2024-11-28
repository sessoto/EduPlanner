from django.http import JsonResponse
from eventos.models import Eventos
from django.shortcuts import render
from django.views.generic import TemplateView



class calendarioView(TemplateView):
    template_name= "calendario.html"

def api_eventos(request):
    
    lista = Eventos.objects.all()
    data = {
         [
            {
                "nombre": evento.nombre,
                "descripcion": evento.descripcion,
                "fecha": evento.fecha.isoformat(),

            }
            for evento in lista
        ]
    }
    return JsonResponse(data)


def calendario_admin(request):
    return render(request, 'calendario_admin.html')



