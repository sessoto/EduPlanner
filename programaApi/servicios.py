import requests

api_url = "https://calendarific.com/api/v2"
api_key= "5jR5Y8PuOfjietfT6yDgmEdIkoPaYYK9"
def obtener_feriados():
    try:
        respuesta = requests.get(api_url, headers={"Authorization": f"Bearer {api_key}"})
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            return {"error": f"Error al conectar con la API: {respuesta.status_code}"}
    except requests.RequestException as e:
        return {"error": str(e)}