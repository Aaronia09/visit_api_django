from rest_framework import viewsets
from hotel.models import city, hotel, roomtype
from hotel.serializers import citySerializer, hotelSerializer, roomtyperializer



class roomtypeViewSet(viewsets.ModelViewSet):
    queryset = roomtype.objects.all()
    serializer_class = roomtyperializer


class hotelViewSet(viewsets.ModelViewSet):
    queryset = hotel.objects.all()
    serializer_class = hotelSerializer


class cityViewSet(viewsets.ModelViewSet):
    queryset = city.objects.all()
    serializer_class = citySerializer