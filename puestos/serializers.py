from rest_framework.serializers import ModelSerializer

from puestos.models import Puesto

class PuestoSerializer(ModelSerializer):
    class Meta:
        model = Puesto
        fields = ('id', 'cargo', 'area')