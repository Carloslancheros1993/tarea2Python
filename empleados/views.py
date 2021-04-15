from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from empleados.models import Empleado
from empleados.serializers import EmpleadoSerializer, DetailEmpleadoSerializer


class EmpleadoGenericView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoViewSet(ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def get_serializer_class(self, *args, **kwargs):
       if self.action == 'retrieve':
          return DetailEmpleadoSerializer

       return EmpleadoSerializer
