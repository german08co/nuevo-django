
from django.shortcuts import render
from inicio.models import Zapatillas


def inicio(request):
       
   return render(request, 'inicio/inicio.html', {})


def zapatillas(request):
    
    return render(request, 'inicio/zapatillas.html')
 
 
 
def crear_zapatillas(request):
   
   if request.method == 'POST':
      
      marca = request.POST.get('marca')
      descripcion = request.POST.get('descripcion')
      año = request.POST.get('anio')
   
      zapatilla = Zapatillas(marca=marca, descripcion=descripcion, año=año)
      zapatilla.save()
    
   return render(request, 'inicio/crear_zapatillas.html', {})