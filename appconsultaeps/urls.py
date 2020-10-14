#Django
from django.urls import path

#Views
from .views import *

urlpatterns = [
    path('paciente/create', PacienteCreate.as_view(), name='paciente_create'),
<<<<<<< Updated upstream
    path('crear_citas/',CrearCitas.as_view(),name='crear_citas'),
=======
    path('crear_citas/', CrearCitas.as_view(), name='crear_citas')
>>>>>>> Stashed changes
]