from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destino

# Create your views here.
def index(request, *args):

    # Consulta de todos los registros
    destinos = Destino.objects.all()

    return render(request, 'index.html', context={'destinos': destinos})

def create(request):
    if request.method == 'POST':
        newDestino = Destino()

        newDestino.nombre = request.POST.get('nombre')
        newDestino.descripcion = request.POST.get('descripcion')
        newDestino.precioTour = request.POST.get('precioTour')

        newDestino.imagen = request.FILES.get('imagen')

        newDestino.save()

    return redirect('index')

def show(request, id):
    try:

        destino = Destino.objects.get(pk=id)

        return render(request, 'index.html', context={'destino': destino})
    
    except Destino.DoesNotExist:

        return redirect('index')
    
    