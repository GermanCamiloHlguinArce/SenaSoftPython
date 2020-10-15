#django

from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login

#Forms
from .forms import *

#Models
from .models import *


def user_create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password1'))
            if user:
                login(request, user)
                if request.POST.get('tipo_usuario') == 'M':
                    return redirect('medico_create', id=user.id)
                else:
                    return redirect('paciente_create', id=user.id)
    else:
        form = UserCreationForm()

    return render(request, 'appconsultaeps/user_form.html', {'form': form})
    

def paciente_create(request, id):
    user = User.objects.get(pk=id)
    if request.method == 'POST':
        edad = request.POST.get('edad')
        peso = request.POST.get('peso')
        estatura = request.POST.get('estatura')
        estado_civil = request.POST.get('estado_civil')
        doc = tipo_doc.objects.get(pk=request.POST.get('tipo_doc'))
        paciente = pacientes.objects.create(user=user, edad=edad, peso=peso, estatura=estatura, estado_civil=estado_civil, tipo_doc=doc)
        if paciente:
            return redirect('home')
    return render(request, 'appconsultaeps/user_form.html', {'form': PacienteForm})


def medico_create(request, id):
    user = User.objects.get(pk=id)
    if request.method == 'POST':
        doc = tipo_doc.objects.get(pk=request.POST.get('tipo_doc'))
        Numero_doc = request.POST.get('Numero_doc')
        telefono = request.POST.get('telefono')
        especialist = especialista.objects.get(pk=request.POST.get('especialista'))
        
        medico_create = medico.objects.create(user=user, tipo_doc=doc, Numero_doc=Numero_doc, telefono=telefono, especialista=especialist)
        if medico_create:
            return redirect('home')
    return render(request, 'appconsultaeps/user_form.html', {'form': MedicoForm})