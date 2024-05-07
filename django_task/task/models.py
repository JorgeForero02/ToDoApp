import datetime

from django.db import models
from django.utils import timezone


class Task(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    prioridad = models.IntegerField
    fecha_realizar = models.DateTimeField("fecha a realizar")
    estado = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    def was_published_recently(self):
        return self.fecha_realizar >= timezone.now() - datetime.timedelta(days=1)


class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    def str(self):
        return self.user_name
    
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    def str(self):
        return self.category_name


# Create your models here.
