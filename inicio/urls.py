from django.urls import path
from inicio.views import inicio, zapatillas, crear_zapatillas


urlpatterns = [
    
    path('', inicio,name='inicio'),
    path('zapatillas/', zapatillas, name='zapatillas'),
    path('zapatillas/crear/', crear_zapatillas, name='crear_zapatillas')
    
    
]
