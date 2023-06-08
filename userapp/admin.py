from django.contrib import admin

from userapp.models import *


@admin.register(Destinations)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['__str__']



@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'duration')


@admin.register(Flights)
class FlightsAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(FlightClass)
class FlightClassAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    list_display = ['__str__']


# admin.site.register(Hotels)


@admin.register(Participants)
class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ['__str__']
