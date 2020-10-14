#django
from django.shortcuts import render
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
from django.views.generic import FormView
from django.urls import reverse_lazy

#Forms
<<<<<<< Updated upstream
from .forms import *

from .models import *

=======
from .forms import PacienteForm
>>>>>>> Stashed changes

from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView,CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
<<<<<<< Updated upstream
=======
from .Forms import CitasForm
>>>>>>> Stashed changes

class CrearCitas(CreateView):
    Model = 'Citas'
    template_name = 'appconsultaeps/Citas.html'
<<<<<<< Updated upstream
    form_class=CitasForm
=======
    form_class= CitasForm
    success_url = reverse_lazy('index')



#Models
from .models import pacientes
>>>>>>> Stashed changes


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
