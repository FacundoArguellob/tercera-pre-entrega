from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ]
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=60)
    fecha_inicio = models.CharField(max_length=20)
    fecha_fin = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)