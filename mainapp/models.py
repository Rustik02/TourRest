import os
from datetime import timedelta
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name = models.CharField('Country name', max_length=20)
    image = models.ImageField('Image of country', upload_to='images/country')

    def __str__(self):
        return self.name


class TourType(models.Model):
    name = models.CharField('Tour type', max_length=20)

    def __str__(self):
        return self.name


class Tour(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')
    image = models.ImageField('Image', upload_to='images/tour')
    title = models.CharField('Title', max_length=30)
    grade = models.ForeignKey(TourType, on_delete=models.CASCADE, related_name='grade')
    price = models.DecimalField('Price', max_digits=5, decimal_places=2)
    description = models.TextField('Description')

    def __str__(self):
        return self.title


def tour_detail_image_path(instance, filename):
    # Получение имени файла
    filename_base, filename_ext = os.path.splitext(filename)
    # Получение имени папки тура, используя его ID
    tour_folder = 'tour_{}'.format(instance.tour_id)
    # Собираем путь для сохранения изображения
    return os.path.join('images/tour_detail', tour_folder, filename)


class DifficultyLevel(models.Model):
    name = models.CharField('Level name', max_length=20)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField('Season name', max_length=20)

    def __str__(self):
        return self.name


class TourDetail(models.Model):
    tour = models.OneToOneField(Tour, on_delete=models.CASCADE, related_name='tour')
    duration = models.PositiveIntegerField('Duration (days)')
    group_size = models.PositiveIntegerField('Group size')
    difficulty_level = models.ForeignKey(DifficultyLevel, on_delete=models.SET_NULL, null=True,
                                         verbose_name='Difficulty level')
    start_date = models.DateField('Start date', default=timezone.now)
    seasons = models.ManyToManyField(Season, verbose_name='Seasons')
    itinerary = models.TextField('Itinerary')
    highlights = models.TextField('Highlights')
    price_includes = models.TextField('Price includes')
    image1 = models.ImageField('Image', upload_to=tour_detail_image_path)
    image2 = models.ImageField('Image', upload_to=tour_detail_image_path)
    image3 = models.ImageField('Image', upload_to=tour_detail_image_path)
    image4 = models.ImageField('Image', upload_to=tour_detail_image_path)
    image5 = models.ImageField('Image', upload_to=tour_detail_image_path)

    # Добавьте другие параметры для отдыха на природе, если необходимо

    @property
    def end_date(self):
        return self.start_date + timedelta(days=self.duration - 1)


# User = get_user_model()
#
#
# class CustomUserBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(username=username)
#             # print(user.password)
#         except User.DoesNotExist:
#             return None
#         if password == user.password:
#             return user
#         # if user.check_password(password):
#         #     return user
#
#         return None
#
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None

class Booking(models.Model):
    tour_id = models.PositiveBigIntegerField('Tour ID', blank=True, null=True)
    name = models.CharField('Name', max_length=40, null=True, blank=True)
    phone = models.CharField('Phone number', max_length=20, blank=True, null=True)


class User(AbstractUser):
    first_name = models.CharField("First name", max_length=255, null=True, blank=True)
    last_name = models.CharField("Last name", max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField('About me', blank=True, null=True)
    image = models.ImageField('Image', upload_to='images/users', null=True, blank=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.username
