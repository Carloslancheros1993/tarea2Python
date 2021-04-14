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