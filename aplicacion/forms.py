from django import forms
from .models import *

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email']


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estado'].widget = forms.Select(choices=Tarea.ESTADO_CHOICES)