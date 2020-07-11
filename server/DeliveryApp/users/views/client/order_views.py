from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from users.permission import IsClient, IsRestaurantAdmin
from rest_framework.response import Response
from users.serializers.restaurantadmin.restaurantadmin_restaurant_serializers import RestaurantSerializer, MenuSerializer
from restaurants.models import Restaurant, Menu


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsClient])
def client_list_restaurants(request):
    if request.method == "POST":
        restaurants = Restaurant.objects.all().order_by("name")[request.data["start"]:request.data["end"]]
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsClient | IsRestaurantAdmin])
def client_list_restaurant(request, restaurant_id):
    if request.method == "GET":
        restaurant = Restaurant.objects.filter(id=restaurant_id)
        if len(restaurant) == 0:
            return Response("No restaurant with this id.", status=status.HTTP_400_BAD_REQUEST)
        serializer = RestaurantSerializer(restaurant[0])
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsClient | IsRestaurantAdmin])
def client_list_restaurant_menus(request, restaurant_id):
    if request.method == "GET":
        restaurant = Restaurant.objects.filter(id=restaurant_id)
        if len(restaurant) == 0:
            return Response("No restaurant with this id.", status=status.HTTP_400_BAD_REQUEST)
        menu = Menu.objects.filter(restaurant_id=restaurant_id)
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

