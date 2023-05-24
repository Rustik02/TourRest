from django.contrib import admin

from userapp.models import *


@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'duration', 'destination')


@admin.register(Destinations)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('country', 'number_of_tours', 'number_of_places')


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination')
