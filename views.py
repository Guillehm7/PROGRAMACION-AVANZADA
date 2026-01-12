from django.shortcuts import render
from .models import PlatoTipico

def lista_platos(request):
    # Obtenemos todos los platos de la base de datos
    platos = PlatoTipico.objects.all()
    # Enviamos los datos al template
    return render(request, 'platos/lista_platos.html', {'platos': platos})

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import PlatoTipico
import json

# Usamos este decorador para asegurar que la cookie CSRF se envíe, necesaria para AJAX
@ensure_csrf_cookie
def interfaz_administrador(request):
    # EVENTO: Si la petición es POST (viene del botón "Guardar" de la ventana modal)
    if request.method == 'POST':
        try:
            # Leemos los datos enviados por JavaScript
            data = json.loads(request.body)
            
            # Creamos el nuevo plato en la base de datos
            nuevo_plato = PlatoTipico.objects.create(
                nombre=data['nombre'],
                region=data['region'],
                precio_sugerido=data['precio'],
                descripcion=data['descripcion']
            )
            # Devolvemos una respuesta de éxito en formato JSON
            return JsonResponse({'status': 'ok', 'message': f'Plato {nuevo_plato.nombre} guardado correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    # VISTA PRINCIPAL (GET): Carga la interfaz inicial
    platos = PlatoTipico.objects.all().order_by('-id') # Los más recientes primero
    return render(request, 'platos/admin_gui.html', {'platos': platos})
