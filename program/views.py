from rest_framework import viewsets
from program.models import program
from .serializers import programSerializer

class programViewSet(viewsets.ModelViewSet):
    queryset = program.objects.all()
    serializer_class = programSerializer
