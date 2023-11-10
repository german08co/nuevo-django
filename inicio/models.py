from django.db import models

class Calzados(models.Model):
    tipo_de_calzados = models.CharField(max_length=45, default="")

    descripcion = models.TextField()
    año = models.IntegerField()

    class Meta:
        abstract = True

class Zapatillas(Calzados):
    marca = models.CharField(max_length=30)
    talla = models.CharField(max_length=10, default='16')


    def __str__(self):
        return f"{self.id} - {self.marca} - {self.tipo_de_calzados} - {self.descripcion} - {self.año} - {self.talla}"
    
class Zapatos(Calzados):
    marca = models.CharField(max_length=30)
    talla = models.CharField(max_length=10, default='16')


    def __str__(self):
        return f"{self.id} - {self.marca} - {self.tipo_de_calzados} - {self.descripcion} - {self.año} - {self.talla}"

class Ojotas(Calzados):
    marca = models.CharField(max_length=30)
    talla = models.CharField(max_length=10, default='16')


    def __str__(self):
        return f"{self.id} - {self.marca} - {self.tipo_de_calzados} - {self.descripcion} - {self.año} - {self.talla}"
    

