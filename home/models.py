from dataclasses import field
from unittest.util import _MAX_LENGTH
from django.db import models
from pkg_resources import require

# Create your models here.
class Humano(models.Model):
    #atributos a tener
    nombre= models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha_creacion =models.DateTimeField(null=True)
    
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'