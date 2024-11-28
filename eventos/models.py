from django.db import models
from django.db.models import Model
class Eventos(Model):
    # Columnas de la tabla evento
    nombre = models.CharField(max_length=100) 
    descripcion = models.TextField() 
    fecha = models.DateField() 
    

    def __str__(self):
        return self