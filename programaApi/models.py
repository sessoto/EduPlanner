from django.db import models

class Feriado(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.fecha})"