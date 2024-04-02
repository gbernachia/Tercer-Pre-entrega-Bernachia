from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=40)
    presentacion = models.IntegerField()

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    cuit = models.IntegerField()

class Profesional(models.Model):
    nombre = models.CharField(max_length=40)
    cuit = models.IntegerField()