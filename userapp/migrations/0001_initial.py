# Generated by Django 4.2.1 on 2023-06-01 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=40, null=True, verbose_name='Country')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('image', models.ImageField(default=None, upload_to='media/images/destinations', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Destination',
                'verbose_name_plural': 'Destinations',
            },
        ),
        migrations.CreateModel(
            name='FlightClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Class name')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'FlightClass',
                'verbose_name_plural': 'FlightClasses',
            },
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('end_date', models.DateField(verbose_name='End date')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_flights', to='userapp.destinations')),
                ('flight_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.flightclass')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_flights', to='userapp.destinations')),
            ],
            options={
                'verbose_name': 'Flight',
                'verbose_name_plural': 'Flights',
            },
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.destinations')),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hotels',
            },
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Place Name')),
                ('image', models.ImageField(default=None, upload_to='media/images/places', verbose_name='Image')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='userapp.destinations')),
            ],
            options={
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
            },
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of tour')),
                ('description', models.TextField(blank=True, max_length=50, verbose_name='Description')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('image', models.ImageField(blank=True, default=None, upload_to='media/images/tours', verbose_name='Image')),
                ('price_per_day', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price per day')),
                ('flight_price', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.flights')),
                ('hotel_price', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.hotels')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tours', to='userapp.places')),
            ],
            options={
                'verbose_name': 'Tour',
                'verbose_name_plural': 'Tours',
            },
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('flights', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='userapp.flights')),
                ('hotels', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='userapp.hotels')),
                ('tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='userapp.tours')),
            ],
        ),
    ]
