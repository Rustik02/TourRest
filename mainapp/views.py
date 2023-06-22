from rest_framework.viewsets import ModelViewSet
from mainapp.permission import IsAdminReadOnly
from mainapp.serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView, Response
from django.db.models import Q


class TourDetailView(APIView):
    def get(self, request):
        name = request.GET.get('name')
        date = request.GET.get('date')
        price = request.GET.get('price')

        if name:
            queryset = Tour.objects.filter(Q(country__name=name))

        if date:
            queryset = Tour.objects.filter(Q(date=date))

        if price:
            queryset = Tour.objects.filter(Q(price=price))

        return Response(TourSerializer(queryset, many=True).data)


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
    queryset = Tour.objects.all()
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


class TourDetailViewSet(ModelViewSet):
    queryset = TourDetail.objects.all()
    serializer_class = TourDetailSerializer
    # permission_classes = [IsAdminReadOnly]


class CustomerViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [IsAdminReadOnly]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    # permission_classes = [IsAdminReadOnly]
