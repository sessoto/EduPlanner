from django.http import JsonResponse
from datetime import datetime
import requests

def consultar_feriados(request):
    year = request.GET.get('year')

    if not year:
        return JsonResponse({"error": "Año no proporcionado"}, status=400)

    try:
        api_url = "https://calendarific.com/api/v2/holidays"
        api_key = "5jR5Y8PuOfjietfT6yDgmEdIkoPaYYK9"
        parametros = {
            "api_key": api_key,
            "country": "CL",
            "year": year
        }

        respuesta = requests.get(api_url, params=parametros)
        respuesta.raise_for_status()
        datos = respuesta.json()

        feriados = []
        for feriado in datos["response"]["holidays"]:
            fecha_str = feriado["date"]["iso"]
            fecha_obj = datetime.fromisoformat(fecha_str).date()

            feriados.append({
                "title": feriado["name"],
                "start": fecha_obj.strftime("%Y-%m-%d"),
                "description": feriado.get("description", "Sin descripción"),
                "color": "#FF5733"
            })

        return JsonResponse(feriados, safe=False)

    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Error al consultar los feriados: {e}"}, status=500)
    
    
    