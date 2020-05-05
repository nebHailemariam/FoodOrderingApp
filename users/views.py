from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class DeliveryManViewSet(ModelViewSet):
    serializer_class = DeliveryManSerializer
    queryset = DeliveryMan.objects.all()

class RestaurantAdminViewSet(ModelViewSet):
    serializer_class = RestaurantAdminSerializer
    queryset = RestaurantAdmin.objects.all()

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()