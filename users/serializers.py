from rest_framework.serializers import ModelSerializer
from .models import *

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ("__all__")

class DeliveryManSerializer(ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = ("__all__" )

class RestaurantAdminSerializer(ModelSerializer):
    class Meta:
        model = RestaurantAdmin
        fields = ("__all__")

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")