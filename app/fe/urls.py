# accounts/urls.py
from django.urls import path
from .views import CustomLoginView, HomeView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', HomeView.as_view(), name='home'),
]
