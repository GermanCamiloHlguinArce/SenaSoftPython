#Django
from django.urls import path

#Views
from .views import *

urlpatterns = [
    path('paciente/create', PacienteCreate.as_view(), name='paciente_create'),

    path('crear_citas/',CrearCitas.as_view(),name='crear_citas'),

    path('listar_historia',ListarHistoria.as_view(),name='listar_historia')

]