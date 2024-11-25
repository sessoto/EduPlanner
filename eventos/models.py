from django.db import models

class Evento(models.Model):
    #variables del evento
    nombre = models.CharField(max_length=100) 
    descripcion = models.TextField() 
    fecha_inicio = models.DateField() 
    fecha_fin = models.DateField()  
    es_feriado = models.BooleanField(default=False)  

    def __str__(self):
        return self.nombre