from rest_framework import viewsets
from service.models import accessibilities, service
from service.serializers import accesibilitiesSerializer, serviceSerializer

class serviceViewSet(viewsets.ModelViewSet):
    queryset = service.objects.all()
    serializer_class = serviceSerializer
    
class accessibilitiesViewSet(viewsets.ModelViewSet):
    queryset = accessibilities.objects.all()
    serializer_class = accesibilitiesSerializer