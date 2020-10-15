from django.views.generic import FormView
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
        exclude = ['user']


class MedicoForm(forms.ModelForm):
    class Meta:
        model = medico
        fields = '__all__'
        exclude = ['user']


class UserCreationForm(UserCreationForm):
    Users = [
        ('M', 'Medico'),
        ('P', 'Paciente')
    ]
    tipo_usuario = forms.ChoiceField(required=True, choices=Users)


class HistoriaForm(BSModalModelForm):
    class Meta:
        model= historia_clinica
        fields=['incapacidad','pacientes','motivo_consulta','enfermedades_actual','antecedentes','analisis','plan_manejo']
