from rest_framework import viewsets
from favorites.models import  favorites
from favorites.serializers import favoritesSerializer



class favoritesViewSet(viewsets.ModelViewSet):
    queryset = favorites.objects.all()
    serializer_class=favoritesSerializer