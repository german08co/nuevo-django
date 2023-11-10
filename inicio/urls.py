from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('posteos/', views.posteos, name='posteos'),
    path('logout/', views.exit, name='exit'),
    
    
]
