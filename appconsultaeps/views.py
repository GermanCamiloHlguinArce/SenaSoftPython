#django
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy

#Forms
from .forms import PacienteForm

from .models import *


from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView,CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .Forms import CitasView

class CrearCitas(CreateView):
    Model = 'Citas'
    template_name = 'SenaSoftPython/Citas.html'
    form_class=CitasView


class PacienteCreate(FormView):
    model = pacientes
    form_class = PacienteForm
    template_name = 'appconsultaeps/paciente_form.html'
    success_message = 'Cuenta creada exitosamente!'
    success_url = reverse_lazy('login')


class CrearMedico(CreateView):
    model= medico
    form_class = registro_medicoForm
    template_name = 'registro_medico.html'
