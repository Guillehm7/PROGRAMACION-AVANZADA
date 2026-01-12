from django.urls import path
from . import views

urlpatterns = [
    path('ecuador/platos/', views.lista_platos, name='lista_platos'),
]
