import requests

api_url = "https://calendarific.com/api/v2/holidays"
api_key = "5jR5Y8PuOfjietfT6yDgmEdIkoPaYYK9"

def obtener_feriados(año):
    parametros = {
        "api_key": api_key,
        "country": "CL",
        "year": año,
    }

    try:
        respuesta = requests.get(api_url, params=parametros)
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            return {"error": f"Error al conectar con la API: {respuesta.status_code}"}
    except requests.RequestException as e:
        return {"error": str(e)}