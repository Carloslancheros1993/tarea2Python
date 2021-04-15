from rest_framework.serializers import ModelSerializer

from empleados.models import Empleado
from permisos.serializers import PermisoSerializer
from puestos.serializers import PuestoSerializer

class EmpleadoSerializer(ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class DetailEmpleadoSerializer(ModelSerializer):
    puesto = PuestoSerializer()

    class Meta:
        model = Empleado
        fields = '__all__'