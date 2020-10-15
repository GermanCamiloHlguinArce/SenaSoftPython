#django
from django.shortcuts import render



from django.views.generic import FormView
from django.urls import reverse_lazy

#Forms

from .Forms import *

from .models import *


from .Forms import PacienteForm


from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView,CreateView,ListView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .Forms import CitasForm


class CrearCitas(CreateView):
    Model = 'Citas'
    template_name = 'appconsultaeps/Citas.html'

    form_class=CitasForm


    success_url = reverse_lazy('login')



#Models
from .models import pacientes



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


class ListarHistoria(ListView):
    model = historia_clinica
    template_name = 'appconsultaeps/listar_historia.html'
    context_object_name = 'historias'