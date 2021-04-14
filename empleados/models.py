from django.db import models

from puestos.models import Puesto


class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    puesto = models.ForeignKey(
        Puesto,
        related_name='empleados',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.nombre



