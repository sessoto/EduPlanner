from django.urls import path
from .views import api_eventos

urlpatterns = [
    path('api/', api_eventos, name='api_eventos'),
    ]