from django.shortcuts import render
from .models import PlatoTipico

def lista_platos(request):
    # Obtenemos todos los platos de la base de datos
    platos = PlatoTipico.objects.all()
    # Enviamos los datos al template
    return render(request, 'platos/lista_platos.html', {'platos': platos})
