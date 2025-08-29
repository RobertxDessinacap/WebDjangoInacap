from django.db import models

# Create your models here.
class Contactos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    motivo = models.TextField()
    

    def __str__(self):
        return self.nombre
    

#modelo para  unicamente Roberto
    
class RobertoContacto(models.Model):
    nombre = models.CharField(max_length= 100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    motivo = models.TextField()

    def __str__(self):
        return ("contacto de "+self.nombre)
    

class JuanContacto(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    telefono=models.TextField()
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return ("contacto "+self.nombre)
