from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    comision = models.IntegerField()
    duracion = models.IntegerField()
    descripcion = models.TextField(null=True)

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido},{self.nombre}"

    
class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=200)
    email = models.EmailField()
    profesion = models.CharField(max_length=200)
    bio = models.TextField()

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_de_entrega = models.DateTimeField()
    aprobado = models.BooleanField(default=False)

class Planes(models.Model):
    nombre = models.CharField(max_length=200)
    contenido = models.CharField(max_length=200)
    image = models.URLField()
    autor = models.CharField(max_length=50)
      
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user}"