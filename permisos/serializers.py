from rest_framework.serializers import ModelSerializer

from permisos.models import Permiso

class PermisoSerializer(ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'