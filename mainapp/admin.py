from django.contrib import admin

from mainapp.models import *


@admin.register(User)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone', 'is_staff']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name']


# @admin.register(TourDetailImage)
# class TourDetailImageAdmin(admin.ModelAdmin):
#     list_display = ['id']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'tour']


@admin.register(TourType)
class TourTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['title', 'country', 'price']
    # Другие поля, которые вы хотите отобразить в списке моделей


@admin.register(DifficultyLevel)
class DifficultyLevelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(TourDetail)
class TourDetailAdmin(admin.ModelAdmin):
    list_display = ['tour', 'duration', 'group_size', 'start_date']
    # Другие поля, которые вы хотите отобразить в списке моделей
