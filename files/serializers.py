from rest_framework import serializers
from files.models import files


class filesSerializer(serializers.ModelSerializer):
    class Meta:
        model = files
        fields = '__all__'