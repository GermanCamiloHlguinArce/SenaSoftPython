#Django
from django.urls import path

#Views
from .views import *

urlpatterns = [
    path('paciente/create', PacienteCreate.as_view(), name='paciente_create'),
]