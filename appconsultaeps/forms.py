from django.views.generic import FormView
from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm


from .models import *

class registro_medicoForm(forms.ModelForm):
    class Meta:
        model = medico
        fields = '__all__'


class CitasForm(forms.ModelForm):
    class Meta:
        model= citas
        fields = ['fecha']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].widget.attrs['class'] = 'datetimepicker-input'
        self.fields['fecha'].widget.attrs['data-target'] = '#datetimepicker1'


class PacienteForm(forms.ModelForm):
    class Meta:
        model = pacientes
        fields = '__all__'

class HistoriaForm(BSModalModelForm):
    class Meta:
        model= historia_clinica
        fields=['incapacidad','pacientes','motivo_consulta','enfermedades_actual','antecedentes','analisis','plan_manejo']



class GrupoForm(forms.ModelForm):
    class Meta:
        model=grupo_familiar
        fields=['paciente','medico']
