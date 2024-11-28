from django.http import JsonResponse
from eventos.models import Eventos
from django.shortcuts import render
from django.views.generic import TemplateView


from django.shortcuts import render, redirect
from .models import Eventos

from django.shortcuts import render
from django.http import JsonResponse
from .models import Eventos
from programaApi.models import Feriado  

def cargar_eventos_feriados(request):
    
    eventos = Eventos.objects.all()
    feriados = Feriado.objects.all()

    eventos_data = []
    for evento in eventos:
        eventos_data.append({
            'title': evento.nombre,
            'start': evento.fecha.strftime('%Y-%m-%d'), 
            'description': evento.descripcion,
            'color': '#FF5733'  
        })

    
    feriados_data = []
    for feriado in feriados:
        feriados_data.append({
            'title': feriado.nombre,
            'start': feriado.fecha.strftime('%Y-%m-%d'),  
            'description': feriado.descripcion,
            'color': '#FF0000'  
        })

    
    eventos_feriados = eventos_data + feriados_data

    
    return JsonResponse(eventos_feriados, safe=False)

def crear_evento(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fecha = request.POST.get('fecha')

        
        evento = Eventos(nombre=nombre, descripcion=descripcion, fecha=fecha)
        evento.save()

        
        return redirect('inicio')  
    return render(request, 'calendario.html')


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



