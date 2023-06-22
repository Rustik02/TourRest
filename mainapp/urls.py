from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from TourRest import settings
from mainapp.views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
router = routers.DefaultRouter()
router.register(r'users', CustomerViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'tourtypes', TourTypeViewSet)
router.register(r'tours', TourViewSet)
router.register(r'difficultylevels', DifficultyLevelViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'tourdetails', TourDetailViewSet)
router.register(r'booking', BookingViewSet)
urlpatterns = [
    path('api/v1/', include(router.urls)),
    # path('api/v1/customer-auth', include('rest_framework.urls')),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/tour-detail/', TourDetailView.as_view(), name='tour-detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
