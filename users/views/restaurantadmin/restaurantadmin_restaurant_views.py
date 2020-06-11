from users.permission import IsRestaurantAdmin
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from restaurants.models import Restaurant
from users.serializers.restaurantadmin.restaurantadmin_restaurant_serializers \
    import RestaurantadminRestaurantSerializer


@api_view(['GET'])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_restaurants(request):
    if request.method == "GET":
        restaurants = Restaurant.objects.filter(user=request.user)
        print(restaurants)
        serializer = RestaurantadminRestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsRestaurantAdmin])
def restaurantadmin_restaurant(request, id):
    if request.method == "GET":
        restaurant = Restaurant.objects.filter(id=id, user=request.user)
        serializer = RestaurantadminRestaurantSerializer(restaurant, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        request.data["restaurant"]["id"] = id
        serializer = RestaurantadminRestaurantSerializer(data=request.data["restaurant"])
        if serializer.is_valid(raise_exception=ValueError) or serializer.is_valid(raise_exception=Exception):
            restaurant = Restaurant.objects.get(user=request.user, id=id)
            restaurant.name = serializer.validated_data["name"]
            restaurant.description = serializer.validated_data["description"]
            restaurant.save()
            serializer = RestaurantadminRestaurantSerializer(restaurant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
