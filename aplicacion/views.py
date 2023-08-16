from django.http import HttpResponse
from django.shortcuts import render

from .forms import *
from aplicacion.models import *

# Create your views here.


def usuarios(request):
    resultado_usuarios = []

    if request.method == 'POST':
        usuarios_form = UsuariosForm(request.POST)
        if usuarios_form.is_valid():
            usuarios_form.save()
    else:
        usuarios_form = UsuariosForm()

        buscar = request.GET.get('buscar')
        print(buscar)
        if buscar:
            resultado_usuarios = Usuario.objects.filter(nombre__icontains=buscar)

    usuarios_print = Usuario.objects.all()

    return render(request, 'usuarios.html', {'usuarios_form': usuarios_form, 'usuarios_print': usuarios_print, 'resultado_usuarios': resultado_usuarios})


def tareas(request):
    if request.method == 'POST':
        print('flag')
        tareas_form = TareaForm(request.POST)
        if tareas_form.is_valid():
            tareas_form.save()
    else:
        
        tareas_form = TareaForm()

    return render(request, 'tareas.html', {'tareas_form': tareas_form, "tareas_print": Tarea.objects.all()})


def proyectos(request):
    if request.method == 'POST':
        proyecto_form = ProyectoForm(request.POST)
        if proyecto_form.is_valid():
            proyecto_form.save()
    else:
        proyecto_form = ProyectoForm()
    
    return render(request, 'proyectos.html', {'proyecto_form': proyecto_form, "proyectos_print": Proyecto.objects.all()})
