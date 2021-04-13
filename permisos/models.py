from django.db import models
from empleados.models import Empleado

class Permiso(models.Model):
    dias = models.IntegerField()
    remunerado = models.BooleanField()
    empleado = models.ForeignKey(
        Empleado,
        related_name='permisos',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.nombre

