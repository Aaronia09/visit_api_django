from rest_framework import serializers
from files.serializers import filesSerializer
from hotel.serializers import hotelSerializer
from category.serializers import categorySerializer
from pack.models import pack
from program.serializers import programSerializer
from service.serializers import accesibilitiesSerializer, serviceSerializer





class packSerializer(serializers.ModelSerializer):
    class Meta:
        model = pack
        fields = '__all__'

        
class packdetailSerializer(serializers.ModelSerializer):
    hotels=hotelSerializer(many=True,read_only=True)
    inclusions=accesibilitiesSerializer(many=True,read_only=True)
    service=serviceSerializer(many=True,read_only=True)
    files=filesSerializer(many=True,read_only=True)
    category=categorySerializer(many=True,read_only=True)
    program=programSerializer(many=False,read_only=True)
    class Meta:
        model = pack
        fields = '__all__'