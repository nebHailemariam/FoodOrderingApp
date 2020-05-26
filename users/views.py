from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status

class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def post(self, request):
        serializer = ClientViewSet(data=request.data)
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class DeliveryManViewSet(ModelViewSet):
    serializer_class = DeliveryManSerializer
    queryset = DeliveryMan.objects.all()

    def post(self, request):
        serializer = DELIVERYMAN(data=request.data)
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
class RestaurantAdminViewSet(ModelViewSet):
    serializer_class = RestaurantAdminSerializer
    queryset = RestaurantAdmin.objects.all()

    def post(self, request):
        serializer = RestaurantAdmin(data=request.data)
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = Client.objects.all()

    def post(self, request):
        serializer = UserViewSet(data=request.data)
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)