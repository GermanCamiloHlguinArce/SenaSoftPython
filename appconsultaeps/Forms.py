from django.views.generic import FormView
from django import forms


from .models import *

class registro_medicoForm(forms.ModelForm):
    class Meta:
        model = medico
        fields = '__all__'


class CitasForm(forms.ModelForm):
    class Meta:
        model= citas
        fields = ['fecha']


class PacienteForm(forms.ModelForm):
    class Meta:
        model = pacientes
        fields = '__all__'

class HistoriaForm(forms.ModelForm):
    class Meta:
        model= historia_clinica
        fields=['incapacidad','pacientes','motivo_consulta','enfermedades_actual','antecedentes','analisis','plan_manejo']