from django.db import models

# Create your models here.

class cliente (models.Model):
    nombre = models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    ciudad= models.CharField(max_length=20)
    email= models.EmailField()
    

    def __str__(self):
        return f"{self.nombre}, {self.email}"

class mascotas (models.Model):

    nombre_mascota = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    genero= models.CharField(max_length=20)
    edad= models.IntegerField()

    def __str__(self):
        return f"{self.nombre_mascota},{self.tipo}"

class procedimientos (models.Model):
    nombre_proce= models.CharField(max_length=100)
    costo= models.IntegerField()

    def __str__(self):
        return f"{self.nombre_proce},{self.costo}"