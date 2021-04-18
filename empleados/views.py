from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from empleados.models import Empleado
from empleados.serializers import EmpleadoSerializer, DetailEmpleadoSerializer
from permisos.serializers import PermisoSerializer
from puestos.serializers import PuestoSerializer


class EmpleadoGenericView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoViewSet(ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    #Filtrar
    def get_queryset(self):
        data = {}
        for key, value in self.request.query_params.items():
            if key in ['puestos']:
                data[key + '__in'] = value
                continue
            data[key + '__in'] = value
        print(data)
        return self.queryset.filter(**data)

    def get_serializer_class(self, *args, **kwargs):
       if self.action == 'retrieve':
          return DetailEmpleadoSerializer
       return EmpleadoSerializer


    @action(methods=['GET'], detail=True)
    def puesto(self, request, pk=None):
        empleado = self.get_object()
        serialized = PuestoSerializer(empleado.puesto)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(methods=['GET'], detail=False)
    def ordering(self, request):
        queryset = self.get_queryset().order_by('-nombre')
        serialized = EmpleadoSerializer(queryset, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

'''
    Especialmente para relaciones MANYTOMANY
    @action(methods=['GET', 'POST], detail=True)
    def puestos(self, request, pk=None):
        if request.method == 'GET':
            empleado = self.get_object()
            # empleado = Empleado.objects.get(id=pk)
            puestos = empleado.puestos.all()
            serialized = PuestoSerializer(puestos, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
        )
        
        if request.method == 'POST':
            puestos_id = request.data['puestos']
            print(puestos_id)
            for puesto_id in puestos_id:
                puesto = Puesto.objects.get(id=puesto_id)
                empleado.puestos.add(puesto)
            return Response(status=status.HTTP_200_OK)
'''