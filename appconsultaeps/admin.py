from django.contrib import admin
from .models import *
admin.site.register(pacientes)
admin.site.register(especialista)
admin.site.register(medico)
admin.site.register(citas)
admin.site.register(historia_clinica)
admin.site.register(tipo_doc)
admin.site.register(grupo_familiar)
