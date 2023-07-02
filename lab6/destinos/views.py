from django.shortcuts import render, redirect
from .models import Destino

# Create your views here.
def index(request, *args):

    # Consulta de todos los registros
    destinos = Destino.objects.all()

    return render(request, 'index.html', context={'destinos': destinos, 'message': args})

def create(request):
    if request.method == 'POST':
        newDestino = Destino()

        newDestino.nombre = request.POST.get('nombre')
        newDestino.descripcion = request.POST.get('descripcion')
        newDestino.precioTour = request.POST.get('precioTour')

        newDestino.imagen = request.FILES.get('imagen')

        newDestino.save()

        return redirect('index')
    else:
        return redirect('index')