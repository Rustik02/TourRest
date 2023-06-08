from django.urls import path, include
from rest_framework import routers

from TourRest import settings
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
    path('', index, name='main'),
    path('registration/', registration, name='registration'),
    path('api/v1/', include(router.urls)),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)