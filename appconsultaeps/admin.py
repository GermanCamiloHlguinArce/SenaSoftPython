from django.contrib import admin
from .models import *
admin.site.register(pacientes)
admin.site.register(citas)
admin.site.register(historia_clinica)
admin.site.register(tipo_doc)