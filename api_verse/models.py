from django.db import models

# Create your models here.

class Carros(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    año = models.CharField(max_length=30)
    estado = models.CharField(max_length=30,choices=[("Nuevo","Nuevo"),("Seminuevo","Seminuevo"),("Usado","Usado")])
    fecha_creado = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.marca}--{self.año}--{self.fecha_creado}"
    
class Motos(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    año = models.CharField(max_length=30)
    estado = models.CharField(max_length=30,choices=[("Nuevo","Nuevo"),("Seminuevo","Seminuevo"),("Usado","Usado")])
    fecha_creado = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.marca}--{self.año}--{self.fecha_creado}" 
    
class Bicis(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    año = models.CharField(max_length=30)
    fecha_creado = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.marca}--{self.año}--{self.fecha_creado}"   