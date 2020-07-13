from rest_framework import serializers
from .models import PlaceInfo, PropertyAndGuestInfo, LocationInfo


class PlaceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceInfo
        fields = '__all__'


class PropertyAndGuestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAndGuestInfo
        fields = '__all__'


class LocationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationInfo
        fields = '__all__'
