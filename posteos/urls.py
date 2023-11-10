from django.urls import path
from . import views


urlpatterns = [
    path('crear_posteos', views.creacion_formulario, name='crear_posteos'),
]
