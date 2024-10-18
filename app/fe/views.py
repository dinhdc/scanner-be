# accounts/views.py
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('')


class HomeView(TemplateView):
    template_name = 'accounts/home.html'
