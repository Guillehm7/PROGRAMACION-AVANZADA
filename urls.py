from django.urls import path
from . import views

urlpatterns = [
    path('ecuador/platos/', views.lista_platos, name='lista_platos'),
]

from django.urls import path
from . import views

urlpatterns = [
    # ... tus rutas anteriores ...
    path('admin-gui/', views.interfaz_administrador, name='admin_gui'),
]
