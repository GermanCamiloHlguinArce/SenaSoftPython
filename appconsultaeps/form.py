from django.views.generic import FormViews
from django.urls import reverse_lazy
from django import forms


from .models import *

class registro_medicoForm(forms.ModelForm):
    class Meta:
        model = medico
        Fields ['__all__']
