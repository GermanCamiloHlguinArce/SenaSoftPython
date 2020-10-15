#Django
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Models
from .models import *


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

    
    # first_name = forms.CharField(max_length=45, required=True, label='Nombres')
    # last_name = forms.CharField(max_length=45, required=True, label='Apellidos')

    # class Meta:
    #     model = User
    #     fields = ['first_name', 'last_name', 'username', 'password']
    #     labels = {
    #         'first_name': 'Nombres',
    #         'last_name': 'Apellidos',
    #         'username': 'Email',
    #     }
