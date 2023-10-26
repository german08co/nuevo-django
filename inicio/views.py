
from django.shortcuts import render
from inicio.models import Zapatillas


def inicio(request):
       
   return render(request, 'inicio/inicio.html', {})


def zapatillas(request):
    
    zapatilla = Zapatillas(marca='Asics', descripcion='Running', año=2022)
    zapatilla.save()
    
    return render(request, 'inicio/zapatillas.html', {'zapatilla':zapatilla})