from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from mainapp.models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class TourTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourType
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    grade = TourTypeSerializer()

    class Meta:
        model = Tour
        fields = '__all__'


class DifficultyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifficultyLevel
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


# class TourImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TourDetailImage
#         fields = '__all__'


class TourDetailSerializer(serializers.ModelSerializer):
    tour = TourSerializer()
    difficulty_level = DifficultyLevelSerializer()
    seasons = SeasonSerializer(many=True)
    end_date = serializers.SerializerMethodField()
    # image = TourImageSerializer

    class Meta:
        model = TourDetail
        fields = '__all__'

    def get_end_date(self, obj):
        return obj.end_date


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['password'] = user.password
        token['phone'] = user.phone
        token['address'] = user.address
        token['description'] = user.description
        token['image'] = user.image.url

        return token
