from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Deporte(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    categoría = models.CharField(max_length=50, blank=False)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre}"

class Deportista(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    edad = models.IntegerField(blank=False)

    class Meta:
        ordering = ['apellido']
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Entrenador(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    fechaAlta = models.DateField(blank=False)

    class Meta:
        verbose_name = "Entrenador"
        verbose_name_plural = "Entrenadores"
        ordering = ['apellido']
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
        
class Club(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    domicilio = models.CharField(max_length=50, blank=False)
    
    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubes"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
    
