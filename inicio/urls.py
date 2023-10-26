from django.urls import path
from inicio.views import inicio, zapatillas
urlpatterns = [
    
    path('', inicio),
    path('zapatillas/', zapatillas)
    
    
]
