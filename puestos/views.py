from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from puestos.models import Puesto
from puestos.serializers import PuestoSerializer


class PuestoGenericView(generics.ListCreateAPIView):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer

class PuestoDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer

class PuestoViewSet(ModelViewSet):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer

    def get_queryset(self):
        cargo = self.request.query_params.get('cargo')
        print(self.request.query_params)
        if cargo:
            data = self.queryset.filter(cargo__icontains=cargo)
            return data
        else:
            return self.query

