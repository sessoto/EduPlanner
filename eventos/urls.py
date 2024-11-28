from django.urls import path
from .views import api_eventos, calendarioView
from . import views

urlpatterns = [
    path('api/', api_eventos, name='api_eventos'),
    path('', calendarioView.as_view(), name='inicio'),
    path('crear-evento/', views.crear_evento, name='crear_evento'),
    path('cargar-eventos-feriados/', views.cargar_eventos_feriados, name='cargar_eventos_feriados'),
    ]