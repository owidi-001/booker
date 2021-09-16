from ..models import *
from rest_framework import serializers


class PassengerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class BusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bus
        fields = "__all__"


class RoutesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Routes
        fields = "__all__"


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
