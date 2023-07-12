from rest_framework.serializers import ModelSerializer
from program import serializers
from program.models import program

class programSerializer(serializers.ModelSerializer):
    class Meta:
        model = program
        fields = '__all__'