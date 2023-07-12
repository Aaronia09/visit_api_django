from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from pack.models import pack
from pack.serializers import packSerializer
from program.models import program
from program.serializers import programSerializer

class programViewSet(viewsets.ModelViewSet):
    queryset = program.objects.all()
    serializer_class = programSerializer

class packViewSet(viewsets.ModelViewSet):
    queryset = pack.objects.all()
    serializer_class = packSerializer

    @action(detail=True, methods=['post'])
    def add_to_favorites(self, request, pk=None):
        pack_obj = self.get_object()

        # Vérifie si l'utilisateur est connecté
        if not request.user.is_authenticated:
            return Response("Veuillez vous connecter pour ajouter un pack en favori")

        favorites, created = favorites.objects.get_or_create(users=request.user, packs=pack_obj)

        # Vérifie si le pack est déjà en favori
        if not created and favorites.is_favorited:
            return Response("Le pack est déjà en favori")

        # Marquer le pack comme favori
        favorites.is_favorited = True
        favorites.save()

        return Response("Le pack a été ajouté aux favoris avec succès")


    def list_favorites_packs(user):
  
     # Get the user's favorite packs from the database.
     favorite_packs = user.favorite_packs.all()

  # Return the list of favorite packs.
     return favorite_packs