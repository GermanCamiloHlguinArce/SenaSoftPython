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