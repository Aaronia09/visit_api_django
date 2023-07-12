from rest_framework import serializers
from service.models import accessibilities, service


class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = service
        fields = '__all__'
class accesibilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = accessibilities
        fields = '__all__'