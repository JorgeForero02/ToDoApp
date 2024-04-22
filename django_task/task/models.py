import datetime

from django.db import models
from django.utils import timezone


class Task(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    prioridad = models.IntegerField(max_length=10)
    fecha_realizar = models.DateTimeField("fecha a realizar")
    estado = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    def was_published_recently(self):
        return self.fecha_realizar >= timezone.now() - datetime.timedelta(days=1)

# Create your models here.
