# Generated by Django 4.2.1 on 2023-06-27 15:16

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0017_remove_user_telegram_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='About me')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/users', verbose_name='Image')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='Tour ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Name')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone number')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Country name')),
                ('image', models.ImageField(upload_to='images/country', verbose_name='Image of country')),
            ],
        ),
        migrations.CreateModel(
            name='DifficultyLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Level name')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Season name')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/tour', verbose_name='Image')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='mainapp.country')),
            ],
        ),
        migrations.CreateModel(
            name='TourType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Tour type')),
            ],
        ),
        migrations.CreateModel(
            name='TourDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveIntegerField(verbose_name='Duration (days)')),
                ('group_size', models.PositiveIntegerField(verbose_name='Group size')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Start date')),
                ('itinerary', models.TextField(verbose_name='Itinerary')),
                ('highlights', models.TextField(verbose_name='Highlights')),
                ('price_includes', models.TextField(verbose_name='Price includes')),
                ('image1', models.ImageField(upload_to='images/tour/tourdetail/', verbose_name='Image')),
                ('image2', models.ImageField(upload_to='images/tour/tourdetail/', verbose_name='Image')),
                ('image3', models.ImageField(upload_to='images/tour/tourdetail/', verbose_name='Image')),
                ('image4', models.ImageField(upload_to='images/tour/tourdetail/', verbose_name='Image')),
                ('image5', models.ImageField(upload_to='images/tour/tourdetail/', verbose_name='Image')),
                ('difficulty_level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.difficultylevel', verbose_name='Difficulty level')),
                ('seasons', models.ManyToManyField(to='mainapp.season', verbose_name='Seasons')),
                ('tour', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tour', to='mainapp.tour')),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grade', to='mainapp.tourtype'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.tour')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
