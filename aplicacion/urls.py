from django.urls import path
from .views import *

urlpatterns = [
    path('', usuarios, name='usuarios'),
    path('proyectos', proyectos, name='proyectos'),
    path('tareas', tareas, name='tareas'),
    path('buscar_usuarios', usuarios, name='buscar_usuarios'),
]