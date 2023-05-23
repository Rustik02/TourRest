from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.
class Tours(models.Model):
    name = models.CharField('Name of tour', max_length=50)
    description = models.TextField('Description', max_length=50)
    duration = models.IntegerField('Duration')
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE, related_name='tours')


class Destination(models.Model):
    country = models.CharField("Country", max_length=40)

    @property
    def number_of_places(self):
        return self.places.count()

    @property
    def number_of_tours(self):
        return self.tours.count()


class Places(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='places')
    name = models.CharField("Place Name", max_length=50)
