from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from rest_framework.generics import *
from rest_framework.viewsets import ModelViewSet

from .forms import UserForm
from .permission import IsAdminReadOnly
from .serializer import *


# Create your views here.
class MainView(TemplateView):
    template_name = "index.html"


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    # permission_classes = (IsAdminReadOnly, )


class DestinationViewSet(ModelViewSet):
    queryset = Destinations.objects.all()
    serializer_class = DestinationsSerializes
    # permission_classes = (IsAdminReadOnly,)


class PlacesViewSet(ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializes
    # permission_classes = (IsAdminReadOnly,)


class ToursViewSet(ModelViewSet):
    queryset = Tours.objects.all()
    serializer_class = ToursSerializes
    # permission_classes = (IsAdminReadOnly,)


class FlightsViewSet(ModelViewSet):
    queryset = Flights.objects.all()
    serializer_class = FlightsSerializes
    # permission_classes = (IsAdminReadOnly,)


class FlightClassViewSet(ModelViewSet):
    queryset = FlightClass.objects.all()
    serializer_class = FlightClassSerializes
    # permission_classes = (IsAdminReadOnly,)


class HotelsViewSet(ModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializes
    # permission_classes = (IsAdminReadOnly,)


class ParticipantsViewSet(ModelViewSet):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializes
    # permission_classes = (IsAdminReadOnly,)


# class RegisterUser(TemplateView):
#     form_class = UserForm
#     template_name = "registration.html"
#     success_url = reverse_lazy('main')
def registration(request):
    return render(request, 'registration.html')