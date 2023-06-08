from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'destinations', DestinationViewSet)
router.register(r'places', PlacesViewSet)
router.register(r'tours', ToursViewSet)
router.register(r'flights', FlightsViewSet)
router.register(r'flight-class', FlightClassViewSet)
router.register(r'hotels', HotelsViewSet)
router.register(r'participants', ParticipantsViewSet)
urlpatterns = [
    path('', MainView.as_view(), name='main'),
    # path('registration/', RegisterUser.as_view(), name='registration'),
    path('registration/', registration, name='registration'),
    path('api/v1/', include(router.urls)),
]
