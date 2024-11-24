from django.urls import path
from .views import CalendarioAPIView, EventoAPIView

urlpatterns = [
    # Endpoint para obtener eventos y feriados#
    path('calendario/', CalendarioAPIView.as_view(), name='calendario'),

    # Endpoint para crear eventos#
    path('evento/', EventoAPIView.as_view(), name='evento'),
]