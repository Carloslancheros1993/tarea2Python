from django.db import models

from permisos.models import Permiso
from puestos.models import Puesto


class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    identificacion = models.IntegerField()
    puesto = models.ForeignKey(
        Puesto,
        related_name='empleados',
        on_delete=models.SET_NULL,
        null=True
    )
    permisos = models.ManyToManyField(Permiso, related_name='empleados')

    def __str__(self):
        return self.nombre



