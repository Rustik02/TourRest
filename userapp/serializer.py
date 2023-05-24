from rest_framework.serializers import Serializer

from userapp.models import *


class ToursSerializes(Serializer):
    class Meta:
        model = Tours
        fields = '___all___'


class DestinationsSerializes(Serializer):
    class Meta:
        model = Destinations
        fields = '___all___'


class PlacesSerializes(Serializer):
    class Meta:
        model = Places
        fields = '___all___'


class FlightsSerializes(Serializer):
    class Meta:
        model = Flights
        fields = '___all___'


class ParticipantsSerializes(Serializer):
    class Meta:
        model = Participants
        fields = '___all___'
