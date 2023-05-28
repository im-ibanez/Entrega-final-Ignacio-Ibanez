from tabnanny import verbose
from tkinter import Y
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms
from datetime import datetime


class Juzgado(models.Model):
    JUZGADO_ELEGIR = [
        (1, 'Juzgado 1'),
        (2, 'Juzgado 2'),
        (3, 'Juzgado 3'),
    ]
    numero_juzgado = models.IntegerField(choices=JUZGADO_ELEGIR, unique=True)
    def __str__(self):
        return f"{self.numero_juzgado}"

class Expediente(models.Model):    
    numero = models.CharField(max_length=10)
    año = models.PositiveIntegerField(validators=[MinValueValidator(1000),MaxValueValidator(9999)])
    caratula = models.CharField(max_length=50)
    juzgado = models.ForeignKey(Juzgado, on_delete=models.SET_NULL, null=True, blank=True)
    fechainicioexpediente = models.DateField(null=True, blank=True)
    
    
    class Meta:
        unique_together = ('numero', 'año')

    def __str__(self):
        return f"Expediente {self.numero} / {self.año}"    

# Create your models here.
class Evidencia(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.SET_NULL, null=True, blank=True)
    
    clase = models.CharField(max_length=50, null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    descripcion = models.TextField(max_length=2000, null=True, blank=True)
    # def __str__(self):
    #    expediente_info = f"{self.expediente.numero} / {self.expediente.año}"
     #   return f"Evidencia nro. {self.id} de la causa: {expediente_info}"
