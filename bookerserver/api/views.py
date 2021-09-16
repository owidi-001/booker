from rest_framework import viewsets
from .serializers import *
from ..models import *


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all().order_by('email')
    serializer_class = PassengerSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class RoutesViewSet(viewsets.ModelViewSet):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
