from django.db import models

# Create your models here.


class PlaceInfo(models.Model):
    place_name = models.CharField(max_length=30)
    place_for_guests = models.IntegerField()
    place_location = models.CharField(max_length=40)


class PropertyAndGuestInfo(models.Model):
    guests_to_accommodate = models.IntegerField()
    bedrooms_guests_can_use = models.IntegerField()
    beds_guests_can_use = models.IntegerField()
    total_bedroom_beds = models.IntegerField()
    total_common_space_beds = models.IntegerField()


class LocationInfo(models.Model):
    country = models.CharField(max_length=30)
    street_address = models.CharField(max_length=30)
    apt_address = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField()
