from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from .models import Destino

# Create your views here.
def index(request):

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

def delete(request, id):

    if request.method == 'DELETE':
        try:
            destino = Destino.objects.get(pk=id)

            nombre = destino.nombre

            destino.delete()

            return HttpResponse(f'{nombre} fue eliminado correctamente')
        except Exception:
            return HttpResponseNotFound(f'Id {id} no encontrado')
    else:
        return redirect('index')


def show(request, id):
    try:

        destino = Destino.objects.get(pk=id)

        return render(request, 'index.html', context={'destino': destino})
    
    except Destino.DoesNotExist:

        return redirect('index')

def edit(request):

    try:

        destino = Destino.objects.get(pk=request.POST.get('id'))
        
        destino.nombre = request.POST.get('nombre')
        destino.descripcion = request.POST.get('descripcion')
        destino.precioTour = request.POST.get('precioTour')
        destino.oferta = True if request.POST.get('oferta') else False

        if request.POST.get('oferta'):
            
            destino.descuento = 0 if request.POST.get('descuento') == '' else request.POST.get('descuento')

        if request.FILES.get('imagen') is not None:

            destino.imagen = request.FILES.get('imagen')
        
        destino.save()

        return redirect('index')
        
    except Destino.DoesNotExist:

        return redirect('index')
