from django.forms import CharField
from rest_framework.serializers import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from .models import *


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ToursSerializes(ModelSerializer):
    flight_price = SerializerMethodField()
    hotel_price = SerializerMethodField()
    place = SerializerMethodField()

    def get_place(self, obj):
        return obj.get_place()

    def get_hotel_price(self, obj):
        return obj.get_hotel_price()

    def get_flight_price(self, obj):
        return obj.get_flight_price()

    class Meta:
        model = Tours
        fields = '__all__'


class DestinationsSerializes(ModelSerializer):
    class Meta:
        model = Destinations
        fields = '__all__'


class PlacesSerializes(ModelSerializer):
    destination = SerializerMethodField()

    def get_destination(self, obj):
        return obj.get_destination()

    class Meta:
        model = Places
        fields = '__all__'


class FlightsSerializes(ModelSerializer):
    origin = SerializerMethodField()
    destination = SerializerMethodField()
    flight_class = SerializerMethodField()

    def get_destination(self, obj):
        return obj.destination

    def get_origin(self, obj):
        return obj.origin

    def get_flight_class(self, obj):
        return obj.flight_class

    class Meta:
        model = Flights
        fields = '__all__'


class FlightClassSerializes(ModelSerializer):
    class Meta:
        model = FlightClass
        fields = '__all__'


class HotelsSerializes(ModelSerializer):
    destination = SerializerMethodField()

    def get_destination(self, obj):
        return obj.get_destination()

    class Meta:
        model = Hotels
        fields = '__all__'


class ParticipantsSerializes(ModelSerializer):
    flights = SerializerMethodField()
    tour = SerializerMethodField()
    hotels = SerializerMethodField()

    def get_flights(self, obj):
        return obj.get_flights()

    def get_tour(self, obj):
        return obj.get_tour()

    def get_hotels(self, obj):
        return obj.get_hotels()

    class Meta:
        model = Participants
        fields = '__all__'
