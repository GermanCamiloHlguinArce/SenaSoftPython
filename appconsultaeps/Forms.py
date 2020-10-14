
from django import forms
from .models import *

class CitasView(forms.ModelForm):
	class Meta:
		model =citas
		fields=['fecha']
