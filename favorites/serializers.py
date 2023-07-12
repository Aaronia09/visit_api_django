from rest_framework import serializers
from favorites.models import  favorites



class favoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = favorites
        fields = '__all__'