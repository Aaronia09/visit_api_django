from rest_framework import viewsets

from category.serializers import categorySerializer

from category.models import category

class categoryViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = categorySerializer