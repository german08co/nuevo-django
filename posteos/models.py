from django.contrib.auth.models import User
from django.db import models

class Posteos(models.Model):
    titulo_posteo = models.CharField(max_length=60)
    fecha_posteo = models.DateTimeField(auto_now_add=True)
    redaccion_posteo = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.titulo_posteo} - {self.fecha_posteo} - {self.usuario}"