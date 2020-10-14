from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

class LoginView(LoginView):
    """Login del sistema"""
    template_name = 'login.html'


class HomeView(TemplateView):
    template_name = 'index.html'

