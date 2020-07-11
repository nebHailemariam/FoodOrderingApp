from rest_framework import serializers
from restaurants.constants import MEAL_TYPE_CHOICES

class RestaurantSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True)
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=255, allow_null=True)


class MenuSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True)
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=255, allow_null=True)
    location_id = serializers.IntegerField()
    restaurant_id = serializers.IntegerField()
    available = serializers.BooleanField()
    available_start_date = serializers.DateTimeField(allow_null=True)
    available_end_date = serializers.DateTimeField(allow_null=True)


class LocationSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True)
    restaurant_id = serializers.IntegerField()
    longitude = serializers.DecimalField(decimal_places=True, max_digits=8, allow_null=True)
    latitude = serializers.DecimalField(decimal_places=True, max_digits=8, allow_null=True)


class SubMenuSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True)
    restaurant_id = serializers.IntegerField()
    menu_id = serializers.IntegerField()
    meal_type= serializers.ChoiceField(choices=MEAL_TYPE_CHOICES)
    description = serializers.CharField(max_length=255, allow_null=True)
    available = serializers.BooleanField()
