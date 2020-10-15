#Django
from django.urls import path

#Views
from .views import *

urlpatterns = [
    path('usuario/create', user_create, name='usuario_create'),
    path('paciente/create/<int:id>', paciente_create, name='paciente_create'),
    path('medico/create/<int:id>', medico_create, name='medico_create'),
]