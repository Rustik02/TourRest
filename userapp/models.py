from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.db import models

# Create your models here.


class Destinations(models.Model):
    country = models.CharField('Country', max_length=40, default='Uzbekistan')
    city = models.CharField('City', max_length=50, default='Tashkent')
    image = models.ImageField('Image', upload_to='images/destinations', max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.country}, {self.city}'

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
    name = models.CharField('Place Name', max_length=50)
    image = models.ImageField('Image', upload_to='images/places', max_length=100, default=None)

    def get_destination(self):
        return f'{self.destination.country}, {self.destination.city}'

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self):
        return f'{self.destination} - {self.name}'


class Tours(models.Model):
    name = models.CharField('Name of tour', max_length=50)
    description = models.TextField('Description', max_length=50, blank=True)
    start_date = models.DateField('Start date', blank=True, null=True)
    end_date = models.DateField('End date', blank=True, null=True)
    place = models.ForeignKey('Places', on_delete=models.CASCADE, related_name='tours', blank=True, null=True)
    image = models.ImageField('Image', upload_to='images/tours', max_length=100, default=None, blank=True)
    price_per_day = models.DecimalField('Price per day', max_digits=10, decimal_places=2, blank=True, null=True)
    hotel_price = models.ForeignKey('Hotels', on_delete=models.CASCADE, blank=True, null=True)
    flight_price = models.ForeignKey('Flights', on_delete=models.CASCADE, blank=True)

    def get_place(self):
        return self.place.name

    def get_hotel_price(self):
        return self.hotel_price.price_per_day

    def get_flight_price(self):
        return self.flight_price.flight_class.price

    def __str__(self):
        return f'{self.name} - {self.price_per_day}'

    def duration(self):
        return (self.end_date - self.start_date) + 1

    def total_price(self):
        price_per_day = self.price_per_day + self.hotel_price.calculate_total_price + self.flight_price.calculate_price
        participant_count = self.participants.count
        total_price = price_per_day * self.duration * participant_count
        return total_price

    def price_per_day_with_extras(self):
        price_per_day = self.price_per_day + self.hotel_price + self.flight_price
        return price_per_day

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'


class FlightClass(models.Model):
    name = models.CharField('Class name', max_length=50)
    price = models.DecimalField('Price', max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = 'FlightClass'
        verbose_name_plural = 'FlightClasses'


class Flights(models.Model):
    origin = models.ForeignKey(Destinations, on_delete=models.CASCADE, related_name='origin_flights')
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, related_name='destination_flights')
    start_date = models.DateField('Start date')
    end_date = models.DateField('End date')
    flight_class = models.ForeignKey(FlightClass, on_delete=models.CASCADE)

    def get_flight_class(self):
        return f'{self.flight_class.name}, {self.flight_class.price}'

    def get_origin(self):
        return f'{self.origin.country}, {self.origin.city}'

    def get_destination(self):
        return f'{self.destination.country}, {self.destination.city}'

    def __str__(self):
        return f'{self.origin} - {self.destination} - {self.flight_class}'

    @property
    def members(self):
        return self.participants.count()

    def calculate_price(self):
        flight_price = self.flight_class.price
        if flight_price is None:
            return None
        num_participants = self.members
        total_price = flight_price * num_participants
        return total_price

    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'


class Hotels(models.Model):
    name = models.CharField('Name', max_length=50, blank=True, null=True)
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE)
    price_per_day = models.DecimalField('Price', max_digits=10, decimal_places=2)
    start_date = models.DateField('Start date', blank=True, null=True)
    end_date = models.DateField('End date', blank=True, null=True)

    def get_destination(self):
        return f'{self.destination.country}, {self.destination.city}'

    def __str__(self):
        return f'{self.destination}, {self.name}, {self.price_per_day}'

    def calculate_total_price(self):
        day_price = self.price_per_day
        if day_price is None:
            return None

        num_participants = self.participants.count()

        duration = self.end_date - self.start_date

        total_price = day_price * num_participants * duration.days
        return total_price

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'


class Participants(models.Model):
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    age = models.IntegerField('Age')
    phone = models.CharField('Phone', max_length=20)
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE, related_name='participants', blank=True, null=True)
    flights = models.ForeignKey(Flights, on_delete=models.CASCADE, related_name='participants', null=True, blank=True)
    hotels = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='participants', null=True, blank=True)

    def __str__(self):
        if self.flights and self.tour and self.hotels:
            return f'{self.first_name}, {self.last_name}, ' \
                   f'{self.age}, {self.phone}, {self.flights}, ' \
                   f'{self.hotels}, {self.tour}'
        else:
            return f'{self.first_name}, {self.last_name}, ' \
                   f'{self.age}, {self.phone}'

    def get_flights(self):
        if self.flights:
            return f'{self.flights.origin.country}, {self.flights.origin.city} - ' \
               f'{self.flights.destination.country}, {self.flights.destination.city}'
        else:
            return "Nurbek lox"

    def get_tour(self):
        if self.tour:
            return f'{self.tour.name}'
        else:
            return "Nurbek lox"

    def get_hotels(self):
        if self.hotels:
            return f'{self.hotels.name}'
        else:
            return "Nurbek lox"
