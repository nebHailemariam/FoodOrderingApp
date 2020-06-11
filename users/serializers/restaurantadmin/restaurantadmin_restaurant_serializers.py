from rest_framework import serializers


class RestaurantadminRestaurantSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=255, allow_null=True)