from rest_framework.viewsets import ModelViewSet
from mainapp.permission import IsAdminReadOnly
from mainapp.serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView, Response
from django.db.models import Q


# Create your views here.


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    # permission_classes = [IsAdminReadOnly]


class TourTypeViewSet(ModelViewSet):
    queryset = TourType.objects.all()
    serializer_class = TourTypeSerializer
    # permission_classes = [IsAdminReadOnly]


class TourViewSet(ModelViewSet):
    queryset = Tour.objects.select_related('country').all()
    serializer_class = TourSerializer
    # permission_classes = [IsAdminReadOnly]


class DifficultyLevelViewSet(ModelViewSet):
    queryset = DifficultyLevel.objects.all()
    serializer_class = DifficultyLevelSerializer
    # permission_classes = [IsAdminReadOnly]


class SeasonViewSet(ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    # permission_classes = [IsAdminReadOnly]


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [IsAdminReadOnly]


class TourSearch(ModelViewSet):
    queryset = TourDetail.objects.all()
    serializer_class = TourDetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('query', '')
        date = self.request.query_params.get('date', '')
        price = self.request.query_params.get('price', '')
        if query:
            queryset = queryset.filter(tour__country__name__icontains=query)
        if date:
            queryset = queryset.filter(start_date__icontains=date)
        if price:
            queryset = queryset.filter(tour_price__icontains=price)
        return queryset


# class TourImageViewSet(ModelViewSet):
#     queryset = TourDetailImage.objects.all()
#     serializer_class = TourImageSerializer


class TourDetailViewSet(ModelViewSet):
    queryset = TourDetail.objects.all()
    serializer_class = TourDetailSerializer
    # permission_classes = [IsAdminReadOnly]


class CustomerViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [IsAdminReadOnly]


class CommentAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsAdminReadOnly]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    # permission_classes = [IsAdminReadOnly]
