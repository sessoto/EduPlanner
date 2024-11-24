import requests

def obtener_feriados():
    API_URL = "https://calendarific.com/api/v2/holidays"
    API_KEY = "5jR5Y8PuOfjietfT6yDgmEdIkoPaYYK9" 
    parametros = {
        'api_key': API_KEY,
        'country': 'CL',
        'year': 2024
    }
    respuesta = requests.get(API_URL, params=parametros)
    if respuesta.status_code == 200:
        return respuesta.json().get('response', {}).get('holidays', [])
    return []