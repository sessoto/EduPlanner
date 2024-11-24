from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from eventos.models import Evento
from .utils import obtener_feriados


class CalendarioAPIView(APIView):
    """
    Endpoint que retorna una lista de eventos y feriados.
    """
    def get(self, request):
        # Obtenemos eventos de la base de datos
        eventos = Evento.objects.all().values('titulo', 'descripcion', 'fecha_inicio', 'fecha_fin', 'tipo')
        # Obtenemos feriados desde la API externa
        feriados = obtener_feriados()
        # Retornamos los datos combinados
        return Response({
            'eventos': list(eventos),
            'feriados': feriados,
        })


class EventoAPIView(APIView):
    """
    Endpoint para gestionar la creación de eventos.
    """
    permission_classes = [IsAdminUser]  # Solo los usuarios administradores pueden crear eventos

    def post(self, request):
        # Obtener datos enviados en el cuerpo de la solicitud
        titulo = request.data.get("titulo")
        descripcion = request.data.get("descripcion")
        fecha_inicio = request.data.get("fecha_inicio")
        fecha_fin = request.data.get("fecha_fin")
        tipo = request.data.get("tipo")
        creado_por = request.user  # Usuario que realiza la solicitud

        # Validar campos obligatorios
        if not titulo or not fecha_inicio or not fecha_fin or not tipo:
            return Response(
                {"error": "Los campos 'titulo', 'fecha_inicio', 'fecha_fin' y 'tipo' son obligatorios."},
            )

        try:
            evento = Evento.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                tipo=tipo,
                creado_por=creado_por,
            )
            return Response(
                {
                    "message": "Evento creado exitosamente.",
                    "evento": {
                        "id": evento.id,
                        "titulo": evento.titulo,
                        "tipo": evento.tipo,
                        "fecha_inicio": evento.fecha_inicio,
                        "fecha_fin": evento.fecha_fin,
                    },
                },
            )
        except Exception as e:
            return Response(
                {"error": f"No se pudo crear el evento: {str(e)}"},
            )