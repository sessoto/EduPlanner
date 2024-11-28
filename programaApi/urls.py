from django.urls import path
from . import views

urlpatterns = [
    path('consultar-feriados/', views.consultar_feriados, name='consultar_feriados'),
]