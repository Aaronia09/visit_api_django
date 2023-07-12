from rest_framework import serializers

from hotel.models import city, hotel, roomtype



class hotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = hotel
        fields = '__all__'


class roomtyperializer(serializers.ModelSerializer):
    class Meta:
        model = roomtype
        fields = '__all__'

class citySerializer(serializers.ModelSerializer):
    class Meta:
        model = city
        fields = '__all__'

