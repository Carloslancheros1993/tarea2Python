from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from permisos.models import Permiso
from permisos.serializers import PermisoSerializer


class PermisoGenericView(generics.ListCreateAPIView):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer

class PermisoDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer

class PermisoViewSet(ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer

    # Filtrar
    def get_queryset(self):
        data = {}
        for key, value in self.request.query_params.items():
            if key in ['empleados']:
                data[key + '__in'] = value
                continue
            data[key + '__in'] = value
        print(data)
        return self.queryset.filter(**data)