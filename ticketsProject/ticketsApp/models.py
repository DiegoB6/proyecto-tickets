from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Create your models here.

class Servicio(models.Model):
    servicio= models.CharField(max_length=20)
    def __str__(self):
        return self.servicio

class Tipo(models.Model):
    tipo= models.CharField(max_length=20)
    def __str__(self):
        return self.tipo

class Criticidad(models.Model):
    criticidad= models.CharField(max_length=20)
    def __str__(self):
        return self.criticidad

class Estado(models.Model):
    estado= models.CharField(max_length=20)
    def __str__(self):
        return self.estado

class Rol(models.Model):
    cargo= models.CharField(max_length=20)
    def __str__(self):
        return self.cargo

class Area(models.Model):
    area= models.CharField(max_length=20)
    def __str__(self):
        return self.area


""" class Trabajador(models.Model):
    usuario_nombre = models.CharField(max_length=50)
    contrasena_usuario = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE) 
    area = models.ForeignKey(Area, on_delete=models.CASCADE) 
    def __str__(self):
        return self.usuario_nombre """




class Usuario(models.Model):
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Ticket(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    detalle = models.CharField(max_length=100)
    observacion = models.CharField(max_length=100)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE) 
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE) 
    criticidad = models.ForeignKey(Criticidad, on_delete=models.CASCADE) 
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE) 
    area = models.ForeignKey(Area, on_delete=models.CASCADE) 


