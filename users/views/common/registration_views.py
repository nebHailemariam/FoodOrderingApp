from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from users.models import Client, DeliveryMan, RestaurantAdmin
from users.serializers.common.registration_serializers import ClientRegistrationSerializer, \
    DeliveryManRegistrationSerializer, RestaurantAdminRegistrationSerializer


class RegisterClient(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = ClientRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=201)
        return Response(serializer.error_messages,
                        status=400)


class RegisterDeliveryMan(CreateAPIView):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = DeliveryManRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=201)
        return Response(serializer.error_messages,
                        status=400)


class RegisterRestaurantAdmin(CreateAPIView):
    queryset = RestaurantAdmin.objects.all()
    serializer_class = RestaurantAdminRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RestaurantAdminRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=201)
        return Response(serializer.error_messages,
                        status=400)


