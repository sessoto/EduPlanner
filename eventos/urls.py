from django.urls import path
from .views import api_eventos, calendarioView

urlpatterns = [
    path('api/', api_eventos, name='api_eventos'),
    path('', calendarioView.as_view(), name='inicio'),
    ]