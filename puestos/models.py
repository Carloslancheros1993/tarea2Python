from django.db import models

class Puesto(models.Model):
    cargo = models.CharField(max_length=200)
    area = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

