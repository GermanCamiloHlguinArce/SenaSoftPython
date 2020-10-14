#django

from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy

#Forms
from .forms import PacienteForm

#Models
from .models import pacientes


class PacienteCreate(FormView):
    model = pacientes
    form_class = PacienteForm
    template_name = 'appconsultaeps/paciente_form.html'
    success_message = 'Cuenta creada exitosamente!'
    success_url = reverse_lazy('login')
