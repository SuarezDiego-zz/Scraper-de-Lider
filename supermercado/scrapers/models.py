from django.db import models


class Inventario(models.Model):
    marca = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
