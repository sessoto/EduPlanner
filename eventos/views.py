from django.http import JsonResponse
from eventos.models import Eventos
from django.shortcuts import render
from django.views.generic import TemplateView


from django.shortcuts import redirect
from .models import Eventos


from programaApi.models import Feriado  

def cargar_eventos_feriados(request):
    
    year = request.GET.get('year')
    if not year:
        return JsonResponse({'error': 'Año no proporcionado'}, status=400)

    try:
        year = int(year)
    except ValueError:
        return JsonResponse({'error': 'Año inválido'}, status=400)

    
    eventos = Eventos.objects.filter(fecha__year=year)
    feriados = Feriado.objects.filter(fecha__year=year)

    
import requests
from django.http import JsonResponse
from eventos.models import Eventos
from programaApi.models import Feriado

def cargar_eventos_feriados(request):
    year = request.GET.get('year', None)

    eventos = Eventos.objects.filter(fecha__year=year) if year else Eventos.objects.all()
    eventos_data = [
        {
            'title': evento.nombre,
            'start': evento.fecha.strftime('%Y-%m-%d'),
            'description': evento.descripcion,
            'color': '#007bff'
        }
        for evento in eventos
    ]

    
    try:
        API_KEY = '5jR5Y8PuOfjietfT6yDgmEdIkoPaYYK9'
        response = requests.get(
            f"https://calendarific.com/api/v2/holidays?api_key={API_KEY}&country=CL&year={year}"
        )

        if response.status_code == 200:
            holidays = response.json().get('response', {}).get('holidays', [])
            feriados_data = [
                {
                    'title': holiday['name'],
                    'start': holiday['date']['iso'],
                    'description': holiday['description'] if 'description' in holiday else '',
                    'color': '#FF0000'
                }
                for holiday in holidays
            ]
        else:
            feriados_data = []
            print(f"Error al obtener los feriados de Calendarific: {response.status_code}")

    except Exception as e:
        print(f"Error al conectar con Calendarific: {e}")
        feriados_data = []

    
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



