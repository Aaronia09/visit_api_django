from rest_framework import viewsets
from files.models import files

from files.serializers import filesSerializer


class filesViewSet(viewsets.ModelViewSet):
    queryset = files.objects.all()
    serializer_class = filesSerializer