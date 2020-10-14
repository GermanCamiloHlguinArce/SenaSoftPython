#Django
from django import forms

#Models
from .models import *


class PacienteForm(forms.Form):
    class Meta:
        model = pacientes
        fields = '__all__'