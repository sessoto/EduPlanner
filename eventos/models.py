from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    #tipos de eventos posibles#
    TipoEvento = [
        ('inicio_semestre', 'Inicio de Semestre'),
        ('fin_semestre', 'Fin de Semestre'),
        ('examen', 'Examen'),
        ('feriado', 'Feriado'),
        ('inscripcion', 'Inscripción'),
    ]
    #variables#
    titulo = models.CharField(max_length=200)
    desc = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo = models.CharField(max_length=100, choices=TipoEvento)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} ({self.tipo})"