from django.db import models
    

class Zapatillas(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    año = models.IntegerField()