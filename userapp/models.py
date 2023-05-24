from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.
class Participants(models.Model):
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    age = models.IntegerField('Age')
    phone = models.CharField('Phone', max_length=20)
    tour = models.ForeignKey('Tours', on_delete=models.CASCADE, related_name='participants')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tours(models.Model):
    name = models.CharField('Name of tour', max_length=50)
    description = models.TextField('Description', max_length=50)
    start_date = models.DateField('Start date')
    end_date = models.DateField('End date')
    destination = models.ForeignKey('Destinations', on_delete=models.CASCADE, related_name='tours')
    place = models.ForeignKey('Places', on_delete=models.CASCADE, related_name='tours')
    image = models.ImageField("Image", upload_to='media/images/tours', max_length=100, default=None)
    price_per_day = models.DecimalField('Price per day', max_digits=10, decimal_places=2)
    hotel_price = models.DecimalField('Hotel price', max_digits=10, decimal_places=2)
    flight_price = models.DecimalField('Flight price', max_digits=10, decimal_places=2)

    def duration(self):
        return (self.end_date - self.start_date).days + 1

    def total_price(self):
        price_per_day = self.price_per_day + self.hotel_price + self.flight_price
        participant_count = self.participants.count()
        total_price = price_per_day * self.duration * participant_count
        return total_price

    def price_per_day_with_extras(self):
        price_per_day = self.price_per_day + self.hotel_price + self.flight_price
        return price_per_day

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'


class Destinations(models.Model):
    country = models.CharField("Country", max_length=40)
    image = models.ImageField("Image", upload_to='media/images/destinations', max_length=100, default=None)

    class Meta:
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'

    @property
    def number_of_places(self):
        return self.places.count()

    @property
    def number_of_tours(self):
        return Tours.objects.filter(place__destination=self).count()


class Places(models.Model):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, related_name='places')
    name = models.CharField("Place Name", max_length=50)
    image = models.ImageField("Image", upload_to='media/images/places', max_length=100, default=None)

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'
